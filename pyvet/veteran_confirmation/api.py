"""
Veteran Confirmation API: https://developer.va.gov/explore/verification/docs/veteran_confirmation?version=current
"""
import logging
import requests

from pyvet.creds import API_URL
from pyvet.client import current_session as session

CONFIRMATION_URL = API_URL + "veteran_confirmation/v0/"


def get_status(
    ssn: str = "796-13-0115",
    first_name: str = "Tamara",
    last_name: str = "Ellis",
    birth_date: str = "1967-06-19",
    middle_name: str = "E",
    gender: str = "F",
):
    """Gets a veteran's status.
    Parameters
    ----------
    ssn : str
        The ssn of the veteran.
    first_name: str
        The first name of the veteran.
    last_name : str
        The last name of the veteran.
    birth_date : str
        The birth date of the veteran.
    middle_name : int
        The middle name of the veteran.
    gender : bool
        The gender of the veteran.
    Returns
    -------
    r : json
        Response in json format.
    """
    status_url = CONFIRMATION_URL + "status"
    json_data = dict(
        ssn=ssn,
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        middle_name=middle_name,
        gender=gender,
    )
    try:
        r = session.post(status_url, json=json_data)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)
