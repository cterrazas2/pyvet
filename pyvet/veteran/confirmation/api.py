"""
Veteran Confirmation API: https://developer.va.gov/explore/verification/docs/veteran_confirmation?version=current
"""
import json
import logging
import requests

from pyvet.creds import API_URL
from pyvet.client import current_session as session
from pyvet.json_alias import Json

CONFIRMATION_URL = API_URL + "veteran-confirmation/v1/"


def get_status(
    first_name: str,
    last_name: str,
    birth_date: str,
    middle_name: str,
    gender: str,
    street_address: str,
    city: str,
    zip_code: str,
    state: str,
    country: str,
    home_phone_number: str,
    mothers_maiden_mame: str,
    birth_place_city: str,
    birth_place_state: str,
    birth_place_country: str,
) -> Json:
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
        The street address of the veteran.
    city: str
        The city of the veteran.
    zip_code: str
        The zip code of the veteran.
    state: str
        The state of the veteran.
    country: str
        The country the veteran lives in.
    home_phone_number: str
        Phone number of veteran.
    mothers_maiden_mame: str
        Veteran's mother's maiden name.
    birth_place_city: str
        City of birth for veteran.
    birth_place_state: str
        State of birth for veteran.
    birth_place_country: str
        Country of birth for veteran.
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
        homePhoneNumber=home_phone_number,
        mothersMaidenName=mothers_maiden_mame,
        birthPlaceCity=birth_place_city,
        birthPlaceState=birth_place_state,
        birthPlaceCountry=birth_place_country,
    )
    try:
        r = session.post(status_url, json=json_data)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)
