"""
Veteran Verification API: https://developer.va.gov/explore/verification
"""
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

CONFIRMATION_URL = API_URL + "veteran_confirmation/v0/"
VERIFICATION_URL = API_URL + "veteran_verification/v0/"


def get_status(ssn, first_name, last_name, birth_date, middle_name="", gender="M"):
    """Gets a veteran's status."""
    status_url = CONFIRMATION_URL + "status"
    print(f"status url = {status_url}")
    params = dict(
        ssn=ssn,
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        middle_name=middle_name,
        gender=gender,
    )
    return requests.get(status_url, params=params, headers=API_KEY_HEADER).json()


def get_service_history():
    """Gets a veteran's service history."""
    service_history_url = VERIFICATION_URL + "/service_history"
    return requests.get(service_history_url)


def get_disability_rating():
    """Gets a veteran's disability rating."""
    disability_rating_url = VERIFICATION_URL + "/disability_rating"
    return requests.get(disability_rating_url)


def send_status(ssn, gender, ln, bd, fn, mn):
    """Sends a veteran's confirmation status with required params."""
    data = dict(
        ssn=ssn,
        gender=gender,
        last_name=ln,
        birth_date=bd,
        first_name=fn,
        middle_name=mn,
    )
    status_url = CONFIRMATION_URL + "/status"
    return requests.post(status_url, data=data)
