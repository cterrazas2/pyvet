"""
Facilities  API: https://developer.va.gov/explore/facilities/docs/facilities?version=current
"""
import logging
import pandas as pd
import requests

from pyvet.creds import API_URL
from pyvet.client import current_session as session

FACILITIES_URL = API_URL + "va_facilities/v0"
FACILITIES_QUERY_MSG = """
    Parameter combinations for `/facilities` query:

    You may optionally specify page and per_page with any query. You must specify one of the following parameter combinations:
    bbox[], with the option of any combination of type, services[], or mobile
    ids
    lat and long, with the option of any combination of radius, ids, type, services[], or mobile
    state, with the option of any combination of type, services[], or mobile
    visn
    zip, with the option of any combination of type, services[], or mobile
    """


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
    address: str,
    city: str,
    state: str,
    zip_code: str,
    drive_time: int = None,
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
    bbox: list = None,
    ids: list = None,
    latitude: float = None,
    longitude: float = None,
    radius: float = None,
    facility_type: str = None,
    services: list = None,
    mobile: bool = None,
    state: str = None,
    visn: int = None,
    zip_code: str = None,
    page: int = 1,
    per_page: int = 30,
):
    """Gets all VA Facilities with optional query parameters.
    Parameters
    ----------
    bbox : list
        The bbox to limit the query.
    ids : list
        The ids to limit the query.
    latitude: float
        Latitude for the query.
    longitude: float
        Longitude for th query.
    radius: float
        Radius size to set.
    facility_type: str
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
    page : int
        The number of pages to limit.
    per_page : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    # See FACILITIES_QUERY_MSG above for VA requirement here
    combos_met = (
        (bbox and (facility_type or services or mobile))
        or ids
        or (
            (latitude and longitude)
            and (radius or ids or facility_type or services or mobile)
        )
        or (state and (facility_type or services or mobile))
        or visn
        or (zip_code and (facility_type or services or mobile))
    )
    if combos_met:
        params = dict(
            bbox=bbox,
            ids=ids,
            lat=latitude,
            long=longitude,
            radius=radius,
            type=facility_type,
            services=services,
            mobile=mobile,
            state=state,
            visn=visn,
            zip=zip_code,
            page=page,
            per_page=per_page,
        )
        bbox_url = FACILITIES_URL + "/facilities"
        try:
            r = session.get(bbox_url, params=params)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            logging.error(e)
    else:
        logging.error(FACILITIES_QUERY_MSG)


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
