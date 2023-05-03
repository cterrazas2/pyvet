"""
Veteran Verification API: https://developer.va.gov/explore/verification/docs/veteran_verification?version=current
"""
import logging

import requests

from pyvet.client import (
    current_session as session,
)
from pyvet.client import token_scheduler
from pyvet.creds import API_URL
from pyvet.json_alias import Json

VERIFICATION_URL = API_URL + "veteran_verification/v1/"
VERIFICATION_SCOPE = "profile openid offline_access disability_rating.read service_history.read veteran_status.read"


def get_status() -> Json | None:
    """Gets a veteran's status via oidc.
    Returns
    -------
    r : json
        Response in json format.
    """
    token = token_scheduler.get_bearer_token(va_api="veteran", scope=VERIFICATION_SCOPE)
    session.headers["Authorization"] = f"""Bearer {token}"""
    if session.headers.get("Authorization") is None:
        return None
    # from pprint import pprint

    # print("Getting user info")
    # pprint(token_scheduler.get_user_info(token))
    # print("Introspecting token")
    # pprint(token_scheduler.introspect_token(token))

    status_url = VERIFICATION_URL + "status"
    try:
        r = session.get(status_url, headers=session.headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_disability_rating() -> Json | None:
    """Gets a veteran's disability rating via oidc.
    Returns
    -------
    r : json
        Response in json format.
    """
    session.headers[
        "Authorization"
    ] = f"""Bearer {token_scheduler.get_bearer_token(va_api="veteran", scope=VERIFICATION_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        return None
    disability_rating_url = VERIFICATION_URL + "disability_rating"
    try:
        r = session.get(disability_rating_url, headers=session.headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_service_history() -> Json | None:
    """Gets a veteran's service history via oidc.
    Returns
    -------
    r : json
        Response in json format.
    """
    session.headers[
        "Authorization"
    ] = f"""Bearer {token_scheduler.get_bearer_token(va_api="veteran", scope=VERIFICATION_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        return None
    service_history_url = VERIFICATION_URL + "service_history"
    try:
        r = session.get(service_history_url, headers=session.headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)
