"""
Client module for the VA API.
"""
import logging

import oidc_client as oidc
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from pyvet.creds import (
    API_BACKOFF_FACTOR,
    API_FORCE_LIST,
    API_KEY_HEADER,
    API_RETRIES,
    AUTH_SERVER,
    CLIENT_ID,
    DEFAULT_SCOPE,
    ISSUER,
    REDIRECT,
)


class TokenCache:
    """A simple token cache."""

    def __init__(self):
        self.tokens: dict[str, str] = {}

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
        return token if token else None


def get_bearer_token(va_api: str, scope: str = DEFAULT_SCOPE) -> str | None:
    """Get a bearer token from the VA OIDC server.
    Parameters
    ----------
    scope : str
        A scope to request from the VA OIDC server (different per VA API).
    Returns
    -------
    token : str
        A bearer token.
    """
    try:
        if token_cache.has_token(va_api):
            return token_cache.get_token(va_api)
        logging.error(
            "No token found, requesting a new one for VA %s api.", va_api.capitalize()
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
        token_cache.tokens[va_api] = token.access_token
        return token.access_token
    except Exception as e:
        logging.error(e)


def create_session() -> requests.Session:
    """Create a session with the VA API.
    Returns
    -------
    session : requests.Session:
        A session object with the VA API key.
    """
    session = requests.Session()
    session.headers = API_KEY_HEADER
    retry = Retry(
        total=API_RETRIES,
        read=API_RETRIES,
        connect=API_RETRIES,
        backoff_factor=API_BACKOFF_FACTOR,
        status_forcelist=API_FORCE_LIST,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


current_session = create_session()
token_cache = TokenCache()

if current_session.headers.get("apiKey") == "REPLACE ME":
    logging.error(
        "No API key set, visit: https://developer.va.gov/onboarding/request-sandbox-access"
    )
