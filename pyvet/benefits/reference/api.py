"""
Benefits API: https://developer.va.gov/explore/benefits/docs/benefits_reference_data?version=current
"""
import logging

import requests

from pyvet.client import current_session as session
from pyvet.creds import API_URL
from pyvet.json_alias import Json

BENEFITS_REFERENCE_URL = API_URL + "benefits-reference-data/v1/"


def get_contention_types(
    page: int = 1,
    page_size: int = 30,
) -> Json:
    """Fetches all contention types.
    Parameters
    ----------
    page : int
        The number of pages to limit.
    page_size : int
        Maximum size of page.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "contention-types"
    try:
        r = session.get(ref_url, params={"page": page, "pageSize": page_size})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_countries(
    page: int = 1,
    page_size: int = 30,
) -> Json:
    """Get all countries.
    Parameters
    ----------
    page : int
        The number of pages to limit.
    page_size : int
        Maximum size of page.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "countries"
    try:
        r = session.get(ref_url, params={"page": page, "pageSize": page_size})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_disabilities(
    page: int = 1,
    page_size: int = 30,
) -> Json:
    """Get all VA disabilities.
    Parameters
    ----------
    page : int
        The number of pages to limit.
    page_size : int
        Maximum size of page.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "disabilities"
    try:
        r = session.get(ref_url, params={"page": page, "pageSize": page_size})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_intake_sites(
    page: int = 1,
    page_size: int = 30,
) -> Json:
    """Get all VA intake sites.
    Parameters
    ----------
    page : int
        The number of pages to limit.
    page_size : int
        Maximum size of page.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "intake-sites"
    try:
        r = session.get(ref_url, params={"page": page, "pageSize": page_size})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_military_pay_types(
    page: int = 1,
    page_size: int = 30,
) -> Json:
    """Get all military pay types.
    Parameters
    ----------
    page : int
        The number of pages to limit.
    page_size : int
        Maximum size of page.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "military-pay-types"
    try:
        r = session.get(ref_url, params={"page": page, "pageSize": page_size})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_service_branches(
    page: int = 1,
    page_size: int = 30,
) -> Json:
    """Get all service branches.
    Parameters
    ----------
    page : int
        The number of pages to limit.
    page_size : int
        Maximum size of page.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "service-branches"
    try:
        r = session.get(ref_url, params={"page": page, "pageSize": page_size})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_special_circumstances(
    page: int = 1,
    page_size: int = 30,
) -> Json:
    """Get all special circumstances.
    Parameters
    ----------
    page : int
        The number of pages to limit.
    page_size : int
        Maximum size of page.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "special-circumstances"
    try:
        r = session.get(ref_url, params={"page": page, "pageSize": page_size})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_states(
    page: int = 1,
    page_size: int = 30,
) -> Json:
    """Get all states.
    Parameters
    ----------
    page : int
        The number of pages to limit.
    page_size : int
        Maximum size of page.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "states"
    try:
        r = session.get(ref_url, params={"page": page, "pageSize": page_size})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_treatment_centers(
    state_code: int | None = None,
    page: int = 1,
    page_size: int = 30,
) -> Json:
    """Get all treatments centers.
    Parameters
    ----------
    state_code: : int
        The state to find treatment centers in.
    page : int
        The number of pages to limit.
    page_size : int
        Maximum size of page.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_REFERENCE_URL + "treatment-centers"
    try:
        r = session.get(
            ref_url,
            params={"stateCode": state_code, "page": page, "pageSize": page_size},
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)
