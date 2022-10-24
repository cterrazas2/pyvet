"""
Appeals API (internal use only): https://developer.va.gov/explore/appeals
"""
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

APPEALS_URL = API_URL + "appeals/v0/appeals"


def get_appeals(vet_ssn: str, username: str):
    """Gets appeals for a veteran for a user with optional params.
    Parameters
    ----------
    vet_ssn : str
        Veteran ssn to get appeal
    username : str
        Veteran username to get appeal
    Returns
    -------

    """
    params = {"X-VA-SSN": vet_ssn, "X-VA-User": username}
    return requests.get(APPEALS_URL, params=params, headers=API_KEY_HEADER)
