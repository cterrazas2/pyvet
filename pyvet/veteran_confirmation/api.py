"""
Veteran Confirmation API: https://developer.va.gov/explore/verification/docs/veteran_confirmation?version=current
"""
import logging
import requests

from pyvet.creds import API_URL
from pyvet.client import current_session as session

CONFIRMATION_URL = API_URL + "veteran-confirmation/v1/"


def get_status(
    first_name: str = "Alfredo",
    last_name: str = "Armstrong",
    birth_date: str = "1993-06-08",
    middle_name: str = "M",
    gender: str = "M",
    street_address: str = "17020 Tortoise St",
    city: str = "Round Rock",
    zip_code: str = "78664",
    state: str = "TX",
    country: str = "USA",
):
    """Gets a veteran's status.
    Parameters
    ----------
    first_name: str
        The first name of the veteran.
    last_name : str
        The last name of the veteran.
    birth_date : str
        The birth date of the veteran.
    middle_name : str
        The middle name of the veteran.
    gender : str
        The gender of the veteran.
    street_address: str
        The street adress of the veteran.
    city: str
        The city of the veteran.
    zip_code: str
        The zip code of the veteran.
    state: str
        The state of the veteran.
    Returns
    -------
    r : json
        Response in json format.
    """
    status_url = CONFIRMATION_URL + "status"
    json_data = dict(
        firstName=first_name,
        lastName=last_name,
        birthDate=birth_date,
        middleName=middle_name,
        gender=gender,
        streetAddressLine1=street_address,
        city=city,
        zipCode=zip_code,
        state=state,
        country=country,
    )
    try:
        r = session.post(status_url, json=json_data)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)
