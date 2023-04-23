import logging
import requests

from pyvet.creds import (
    API_BACKOFF_FACTOR,
    API_FORCE_LIST,
    API_KEY_HEADER,
    API_RETRIES,
)
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def create_session():
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
