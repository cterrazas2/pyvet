"""
Veteran Confirmation API: https://developer.va.gov/explore/verification/docs/veteran_confirmation?version=current
"""
import logging
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

CONFIRMATION_URL = API_URL + "veteran_confirmation/v0/"

"""

{
  "ssn": "555-55-5555",
  "first_name": "John",
  "last_name": "Doe",
  "birth_date": "1965-01-01",
  "middle_name": "Theodore",
  "gender": "M"
}
"""


def get_status(
    ssn: str = "796-13-0115",
    first_name: str = "Tamara",
    last_name: str = "Ellis",
    birth_date: str = "1967-06-19",
    middle_name: str = "E",
    gender: str = "F",
):
    """Gets a veteran's status."""
    retries = 0
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
        r = requests.post(status_url, headers=API_KEY_HEADER, json=json_data)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.error(f"Connection timeout, retry #{retries}")
            get_status(ssn, first_name, last_name, birth_date, middle_name, gender)
        else:
            logging.error(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)
