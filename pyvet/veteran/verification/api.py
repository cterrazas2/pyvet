"""
Veteran Verification API: https://developer.va.gov/explore/verification/docs/veteran_verification?version=current
"""
from pyvet.client import (
    current_session as session,
)
from pyvet.client import (
    get_bearer_token,
    session_call,
)
from pyvet.creds import API_URL
from pyvet.json_alias import Json

VERIFICATION_URL = API_URL + "veteran_verification/v1/"
VERIFICATION_SCOPE = "profile openid offline_access disability_rating.read service_history.read veteran_status.read"


@session_call()
def get_status() -> Json | None:
    """Gets a veteran's status via oidc.
    Returns
    -------
    r : json
        Response in json format.
    """
    session.headers[
        "Authorization"
    ] = f"""Bearer {get_bearer_token(va_api="veteran", scope=VERIFICATION_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        return None
    status_url = VERIFICATION_URL + "status"
    return session.get(status_url, headers=session.headers)


@session_call()
def get_disability_rating() -> Json | None:
    """Gets a veteran's disability rating via oidc.
    Returns
    -------
    r : json
        Response in json format.
    """
    session.headers[
        "Authorization"
    ] = f"""Bearer {get_bearer_token(va_api="veteran", scope=VERIFICATION_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        return None
    disability_rating_url = VERIFICATION_URL + "disability_rating"
    return session.get(disability_rating_url, headers=session.headers)


@session_call()
def get_service_history() -> Json | None:
    """Gets a veteran's service history via oidc.
    Returns
    -------
    r : json
        Response in json format.
    """
    session.headers[
        "Authorization"
    ] = f"""Bearer {get_bearer_token(va_api="veteran", scope=VERIFICATION_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        return None
    service_history_url = VERIFICATION_URL + "service_history"
    return session.get(service_history_url, headers=session.headers)
