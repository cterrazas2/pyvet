"""
Veteran Verification API: https://developer.va.gov/explore/verification/docs/veteran-verification?version=current
"""
import logging
import requests

from pyvet.creds import API_URL
from pyvet.client import (
    current_session as session,
    get_bearer_token,
)

VERIFICATION_URL = API_URL + "veteran-verification/v1/"
VERIFICATION_SCOPE = "profile openid offline_access disability_rating.read service_history.read veteran_status.read"


def get_status():
    """Gets a veteran's status via oidc.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(
            va_api="veteran-verification", scope=VERIFICATION_SCOPE
        )
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    status_url = VERIFICATION_URL + "status"
    try:
        r = session.get(status_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_disability_rating():
    """Gets a veteran's disability rating via oidc.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(
            va_api="veteran-verification", scope=VERIFICATION_SCOPE
        )
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    disability_rating_url = VERIFICATION_URL + "disability_rating"
    try:
        r = session.get(disability_rating_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_service_history():
    """Gets a veteran's service history via oidc.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(
            va_api="veteran-verification", scope=VERIFICATION_SCOPE
        )
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    service_history_url = VERIFICATION_URL + "service_history"
    try:
        r = session.get(service_history_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)
