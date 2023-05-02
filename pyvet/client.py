"""
Client module for the VA API.
"""
import logging

# the below is an internal version, with some modifications.
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


def get_bearer_token(scope: str = DEFAULT_SCOPE) -> str | None:
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

if current_session.headers.get("apiKey") == "REPLACE ME":
    logging.error(
        "No API key set, visit: https://developer.va.gov/onboarding/request-sandbox-access"
    )
