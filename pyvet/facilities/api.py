"""
Facilities  API: https://developer.va.gov/explore/facilities/docs/facilities?version=current
"""
import logging
import pandas as pd
import requests

from pyvet.creds import API_URL
from pyvet.client import current_session as session

FACILITIES_URL = API_URL + "va_facilities/v0"


def export_to_csv(file_name: str, data: list):
    """Exports data to a csv file."""
    for i, row in enumerate(data):
        pd_norm = pd.json_normalize(row)
        if i == 0:
            pd_norm.to_csv(file_name)
        else:
            pd_norm.to_csv(file_name, mode="a", header=False)


def get_ids():
    """Gets all VA Facility IDs with optional params.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = dict(type="health")
    ids_url = FACILITIES_URL + "/ids"
    try:
        r = session.get(ids_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_nearby(
    address: str = "",
    city: str = "Los Angeles",
    state: str = "CA",
    zip_code: str = "90073",
    drive_time: int = 60,
    export_csv_file: bool = False,
):
    """Gets all nearby VA Facilities with optional params.
    Parameters
    ----------
    address : str
        The address to start the search.
    city : str
        City name to start the search.
    state : str
        State to start the search.
    zip_code : str
        Zip code to start the search.
    drive_time : int
        The maximum drive time to filter results.
    export_csv_file : bool
        Flag to export nearby facilities into a csv file.

    Returns
    -------
    r : json
        Response in json format.
    """
    params = dict(
        street_address=address,
        city=city,
        state=state,
        zip=zip_code,
        drive_time=drive_time,
    )
    nearby_url = FACILITIES_URL + "/nearby"
    try:
        r = session.get(nearby_url, params=params)
        r.raise_for_status()
        r = r.json()
        if export_csv_file:
            output_file = "nearby.csv"
            csv_data = r.get("data")
            export_to_csv(file_name=output_file, data=csv_data)
            logging.info("Success: Nearby VA Facilities data populated in nearby.csv.")
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_facilities_by_query(
    bbox: list,
    ids: list,
    lat: float,
    long: float,
    radius: float,
    type: str,
    services: list,
    mobile: bool,
    state: str,
    visn: int,
    zip_code: str,
):
    """Gets all VA Facilities with optional query parameters.
    Parameters
    ----------
    bbox : list
        The bbox to limit the query.
    ids : list
        The ids to limit the query.
    lat: float
        Latitude for the query.
    long: float
        Longitude for th query.
    radius: float
        Radius size to set.
    type: str
        Type of facilities of ["health", "benefits", "cemetery", "vet_center"]
    services: list
        Service types to filter query.
    mobile: bool
        For mobile search filter.
    state: str
        State to query.
    visn: int
        VISN search of matching facilities.
    zip_code: str
        Zip code to search for facilities.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = dict(
        bbox=bbox,
        ids=ids,
        lat=lat,
        long=long,
        radius=radius,
        type=type,
        services=services,
        mobile=mobile,
        state=state,
        visn=visn,
        zip=zip_code,
    )
    bbox_url = FACILITIES_URL + "/facilities"
    try:
        r = session.get(bbox_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_all(export_csv_file: bool = False):
    """Gets all VA Facilities with optional params.
    Parameters
    ----------
    export_csv_file : bool
        Flag to export all facilities into a csv file.

    Returns
    -------
    r : json
        Response in json format.
    """
    params = dict(Accept="application/geo+json")
    all_url = FACILITIES_URL + "/facilities/all"
    try:
        r = session.get(all_url, params=params)
        r.raise_for_status()
        r = r.json()
        if export_csv_file:
            output_file = "all_va_facilities.csv"
            csv_data = r.get("features")
            export_to_csv(file_name=output_file, data=csv_data)
            logging.info("Success: Facilities data populated in all_va_facilities.csv.")
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_facility(f_id: str):
    """Gets a VA Facility with required id param.
    Parameters
    ----------
    f_id : str
        Facility id to retrieve.

    Returns
    -------
    r : json
        Response in json format.
    """
    params = dict(id=f_id)
    facility_url = FACILITIES_URL + "/facilities/" + f_id
    try:
        r = session.get(
            facility_url,
            params=params,
        )
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)
