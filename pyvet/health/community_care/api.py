"""
Health API: https://developer.va.gov/explore/health/docs/community_care?version=current
"""
import logging

import requests

from pyvet.creds import API_URL
from pyvet.client import (
    current_session as session,
    get_bearer_token,
)

HEALTH_URL = API_URL + "community-care/v0/eligibility/"
HEALTH_SCOPE = (
    "profile openid offline_access launch/patient patient/CommunityCareEligibility.read"
)


def get_eligibility(patient: str, service_type: str, extended_drive_min: int = None):
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
        token = get_bearer_token(va_api="community-care", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    status_url = HEALTH_URL + "search"
    params = dict(
        patient=patient, serviceType=service_type, extendedDriveMin=extended_drive_min
    )
    try:
        r = session.get(status_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)
