"""
Health API: https://developer.va.gov/explore/health/docs/community_care?version=current
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

HEALTH_URL = API_URL + "community-care/v0/eligibility/"
HEALTH_SCOPE = (
    "profile openid offline_access launch/patient patient/CommunityCareEligibility.read"
)


@session_call()
def get_eligibility(
    patient: str, service_type: str, extended_drive_min: int | None = None
) -> Json:
    """Get community care eligibility for a patient for a particular service type.
    Parameters
    ----------
    patient : str
        The patient's icn.
    service_type : str
        The service type to check eligibility for.
    extended_drive_min : int
        The extended drive time radius in minutes.
    Returns
    -------
    r : json
        Response in json format.
    """
    session.headers[
        "Authorization"
    ] = f"""Bearer {get_bearer_token(va_api="community_care", scope=HEALTH_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        return None
    status_url = HEALTH_URL + "search"
    params = {
        "patient": patient,
        "serviceType": service_type,
        "extendedDriveMin": extended_drive_min,
    }
    return session.get(status_url, headers=session.headers, params=params)
