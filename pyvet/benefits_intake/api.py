"""
Benefits Intake API: https://developer.va.gov/explore/benefits/docs/benefits?version=current
"""
import logging

import requests
from pyvet.client import current_session as session
from pyvet.creds import API_URL

BENEFITS_INTAKE_URL = API_URL + "vba_documents/v1/"


def create_path_to_upload_file():
    """Creates a path to upload a file.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + "uploads"
    try:
        r = session.post(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def upload_file(params: dict, files: str):
    """Upload a file for benefit intake.
    Parameters
    ----------
    params : dict
        The params to extract the location to submit the file upload.
    files: str
        Pointer to files.

    Returns
    -------
    r : json
        Response in json format.
    """
    try:
        r = session.put(params.get("location"), files=files)
        r.raise_for_status()
        if r.status_code == 200:
            return r.json()
        else:
            logging.error(f"Invalid Response status code of {r.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(e)


def bulk_status_report(guids: list):
    """Retrieves a bulk status report of all reports uploaded.
    Parameters
    ----------
    guids : list
        The list of guids to get a status.
    Returns
    -------
    r : json
        Response in json format.
    """
    status_url = BENEFITS_INTAKE_URL + "uploads/report"
    try:
        r = session.post(status_url, json=dict(ids=guids))
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_uploaded_document(doc_id: str):
    """Get an uploaded document.
    Parameters
    ----------
    doc_id : str
        The doc id to fetch.

    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + f"uploads/{doc_id}"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def download_uploaded_document(doc_id: str):
    """Downloads a previously uploaded document.
    Parameters
    ----------
    doc_id : str
        The doc id of the document to download.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + f"uploads/{doc_id}/download"
    try:
        r = session.get(ref_url)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)
