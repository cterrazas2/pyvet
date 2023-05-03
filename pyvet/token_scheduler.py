"""The token scheduler module."""

import logging
import time

import oidc_client as oidc
import requests

from pyvet.creds import (
    AUTH_SERVER,
    CLIENT_ID,
    DEFAULT_SCOPE,
    ISSUER,
    REDIRECT,
)


class TokenScheduler:
    """A simple token scheduler."""

    def __init__(self, session: requests.Session | None = None):
        self.tokens: dict[str, oidc.oauth.TokenResponse] = {}
        self.current_session = session

    def has_token(self, va_api: str) -> bool:
        """Check if a token exists for a VA API.
        Parameters
        ----------
        va_api : str
            The VA API to check for a token.
        Returns
        -------
        has_token : bool
            Whether or not a token exists for the VA API.
        """
        has_token = va_api in self.tokens
        return has_token

    def get_token(self, va_api: str) -> str | None:
        """Get a token for a VA API.
        Parameters
        ----------
        va_api : str
            The VA API to get a token for.
        Returns
        -------
        token : str
            A bearer token.
        """
        token = self.tokens.get(va_api)
        # Check if token is expired
        if token and self.is_token_expired(token):
            new_token = self.fetch_new_token(va_api)
            return new_token.access_token if new_token else None
        return token.access_token if token else None

    def is_token_expired(self, token: oidc.oauth.TokenResponse) -> bool:
        """Check if a token is expired.
        Parameters
        ----------
        token : oidc.oauth.TokenResponse
            A token.
        Returns
        -------
        is_expired : bool
            Whether or not the token is expired.
        """
        # This should get replaced with a check against the token introspection endpoint.
        return time.time() > token.expires_at

    def fetch_new_token(self, va_api: str) -> oidc.oauth.TokenResponse | None:
        """Fetch a new token using the refresh token for a client.
        Parameters
        ----------
        va_api : str
            The VA API to get a token for.
        """
        token = self.tokens.get(va_api)
        if token is None:
            logging.error("No token found.")
            return None
        params = {
            "grant_type": "refresh_token",
            "refresh_token": token.refresh_token,
            "client_id": CLIENT_ID,
            "scope": token.scope,
        }
        response = requests.post(
            f"{AUTH_SERVER}/token",
            params=params,
            timeout=5,
        )
        if response.status_code != 200:
            logging.error("Token refresh failed.")
            return None
        try:
            token = oidc.oauth.TokenResponse(**response.json())
            self.tokens[va_api] = token
            return token
        except TypeError as e:
            logging.error(e)
            return None

    def introspect_token(self, token: str) -> dict:
        """Introspect a token to see if it is active, can be expired or revoked.
        Parameters
        ----------
        token : str
            A bearer token.
        """
        response = requests.post(
            f"{AUTH_SERVER}/introspect",
            data={"token": token},
            params={"client_id": CLIENT_ID},
            timeout=5,
        )
        if response.status_code != 200:
            logging.error("Token introspect failed.")
            return {}
        return response.json()

    def get_user_info(self, token: str) -> dict:
        """Get user info from a token.
        Parameters
        ----------
        token : str
            A bearer token.
        """
        if self.current_session is None:
            logging.error("No session found.")
            return {}
        self.current_session.headers["Authorization"] = f"""Bearer {token}"""
        try:
            response = self.current_session.get(
                "https://sandbox-api.va.gov/oauth2/userinfo"
            )
            if response.status_code != 200:
                logging.error("User info request failed.")
                return {}
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(e)
            return {}

    def manage_tokens(self) -> dict:
        """Manage tokens."""
        if self.current_session is None:
            logging.error("No session found.")
            return {}
        try:
            response = self.current_session.get(
                "https://sandbox-api.va.gov/oauth2/manage"
            )
            if response.status_code != 200:
                logging.error("Token management request failed.")
                return {}
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(e)
            return {}

    def get_bearer_token(self, va_api: str, scope: str = DEFAULT_SCOPE) -> str | None:
        """Get a bearer token from the VA OIDC server.
        Parameters
        ----------
        va_api : str
            The VA API to request a token for.
        scope : str
            A scope to request from the VA OIDC server (different per VA API).
        Returns
        -------
        token : str
            A bearer token.
        """
        try:
            if self.has_token(va_api):
                return self.get_token(va_api)
            logging.error(
                "No token found, requesting a new one for VA %s api.",
                va_api.capitalize(),
            )
            token = oidc.login(
                provider_config=oidc.config.ProviderConfig(
                    issuer=ISSUER,
                    authorization_endpoint=f"{AUTH_SERVER}/authorization",
                    token_endpoint=f"{AUTH_SERVER}/token",
                ),
                client_id=CLIENT_ID,
                redirect_uri=REDIRECT,  # update this later
                scope=scope,
                interactive=True,
            )
            if token is None:
                logging.error("Fetching token failed.")
                return None
            # token["expires_at"] = token["expires_in"] + time.time()
            self.tokens[va_api] = token
            return token.access_token
        except Exception as e:
            logging.error(e)
