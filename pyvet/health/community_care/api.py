"""
Health API: https://developer.va.gov/explore/health/docs/community_care?version=current
"""
import logging

import requests

from pyvet.client import (
    current_session as session,
)
from pyvet.client import (
    get_bearer_token,
)
from pyvet.creds import API_URL
from pyvet.json_alias import Json

HEALTH_URL = API_URL + "community-care/v0/eligibility/"
HEALTH_SCOPE = (
    "profile openid offline_access launch/patient patient/CommunityCareEligibility.read"
)


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
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return None
        session.headers["Authorization"] = f"Bearer {token}"
    status_url = HEALTH_URL + "search"
    params = {
        "patient": patient,
        "serviceType": service_type,
        "extendedDriveMin": extended_drive_min,
    }
    try:
        r = session.get(status_url, headers=session.headers, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)
