"""
Veteran Verification API: https://developer.va.gov/explore/verification
"""
import logging
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

VERIFICATION_URL = API_URL + "veteran_verification/v1/"


def get_service_history():
    """Gets a veteran's service history."""
    service_history_url = VERIFICATION_URL + "/service_history"
    return requests.get(service_history_url)


def get_disability_rating():
    """Gets a veteran's disability rating."""
    disability_rating_url = VERIFICATION_URL + "/disability_rating"
    return requests.get(disability_rating_url)


def get_status(ssn, gender, ln, bd, fn, mn):
    """Sends a veteran's confirmation status with required params."""
    data = dict(
        ssn=ssn,
        gender=gender,
        last_name=ln,
        birth_date=bd,
        first_name=fn,
        middle_name=mn,
    )
    status_url = VERIFICATION_URL + "/status"
    return requests.post(status_url, data=data)
