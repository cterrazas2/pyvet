"""
Benefits API: https://developer.va.gov/explore/benefits/docs/benefits_reference_data?version=current
"""
import logging
import requests

from pyvet.client import current_session as session
from pyvet.creds import API_URL

BENEFITS_REFERENCE_URL = API_URL + "benefits-reference-data/v1/"


def get_contention_types():
    """Get all contention types.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "contention-types"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_countries():
    """Fetches all countries.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "countries"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_disabilities():
    """Get all VA disabilities.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "disabilities"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_intake_sites():
    """Get intake sites across the country.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "intake-sites"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_military_pay_types():
    """Get all military pay types.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "military-pay-types"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_service_branches():
    """Get all service branches.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "service-branches"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_special_circumstances():
    """Get all special circumstances.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "special-circumstances"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_states():
    """Get all states.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "states"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_treatment_centers():
    """Get all treatments centers.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "treatment-centers"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)
