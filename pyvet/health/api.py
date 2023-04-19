"""
Health API: https://developer.va.gov/explore/health
"""
import logging

import requests

from pyvet.creds import API_URL
from pyvet.client import current_session as session

HEALTH_URL = API_URL + "provider-directory/v0/r4/"


def get_location(
    resource_id: str,
    identifier: str = None,
    address: str = None,
    city: str = None,
    state: str = None,
    zip_code: str = None,
    name: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets provider's location.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    address : str
        The address of the medical facility.
    city : str
        The city of the medical facility.
    state : str
        The state of the medical facility.
    zip_code : str
        The zip code of the of medical facility.
    name : str
        Name of the department within the medical facility.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {
        "_id": resource_id,
        "identifier": identifier,
        "address": address,
        "address-city": city,
        "address-state": state,
        "address-postalcode": zip_code,
        "name": name,
        "page": page,
        "_count": count,
    }
    ids_url = HEALTH_URL + "Location"
    try:
        r = session.get(ids_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_location_by_id(resource_id: str):
    """Gets provider's location.
    Parameters
    ----------
    resource_id: str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    ids_url = HEALTH_URL + f"Location/{resource_id}"
    try:
        r = session.get(ids_url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_organization(
    resource_id: str,
    identifier: str = None,
    address: str = None,
    city: str = None,
    state: str = None,
    zip_code: str = None,
    name: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets an organization's location.
    Parameters
    ----------
    resource_id: str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    address : str
        The address of the organization.
    city : str
        The city of the organization.
    state : str
        The state of the organization.
    zip_code : str
        The zip code of the organization.
    name : str
        Name of the department within the organization.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {
        "_id": resource_id,
        "identifier": identifier,
        "address": address,
        "address-city": city,
        "address-state": state,
        "address-postalcode": zip_code,
        "name": name,
        "page": page,
        "_count": count,
    }
    org_url = HEALTH_URL + "Organization"
    try:
        r = session.get(org_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_organization_by_id(resource_id: str):
    """Gets an organization's location.
    Parameters
    ----------
    resource_id: str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    org_url = HEALTH_URL + f"Organization/{resource_id}"
    try:
        r = session.get(org_url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner(
    resource_id: str,
    identifier: str = None,
    family: str = None,
    given: str = None,
    name: str = None,
    page: int = 1,
    count: int = 30,
):
    """Get practitioner role
    Parameters
    ----------
    resource_id: str
        The logical id of the resource.
    identifier: str
        The logical identifier of the resource.
    family: str
        The name of the practitioner role to locate.
    given: str
        The name of the practitioner role to locate.
    name: str
        The name of the practitioner role to locate.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {
        "_id": resource_id,
        "identifier": identifier,
        "family": family,
        "given": given,
        "name": name,
        "page": page,
        "_count": count,
    }
    pr_role_url = HEALTH_URL + "Practitioner"
    try:
        r = session.get(pr_role_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner_by_id(resource_id: str):
    """Get practitioner by id.
    Parameters
    ----------
    resource_id: str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    pr_id_url = HEALTH_URL + f"Practitioner/{resource_id}"
    try:
        r = session.get(pr_id_url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner_role(
    resource_id: str,
    identifier: str = None,
    name: str = None,
    page: int = 1,
    count: int = 30,
):
    """Get practitioner role
    Parameters
    ----------
    resource_id: str
        The logical id of the resource.
    identifier: str
        The id of the practitioner role to locate.
    name: str
        The name of the practitioner role to locate.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {
        "_id": resource_id,
        "practitioner.identifier": identifier,
        "practitioner.name": name,
        "page": page,
        "_count": count,
    }
    pr_role_url = HEALTH_URL + "PractitionerRole"
    try:
        r = session.get(pr_role_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner_role_by_id(resource_id: str):
    """Get practitioner role by id.
    Parameters
    ----------
    resource_id: str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    pr_role_id_url = HEALTH_URL + f"PractitionerRole/{resource_id}"
    try:
        r = session.get(pr_role_id_url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)
