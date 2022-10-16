"""
Benefits Intake API: https://developer.va.gov/explore/benefits/docs/benefits?version=current
"""
import logging

import requests
from pprint import pprint
from pyvet.creds import API_KEY_HEADER, API_URL

BENEFITS_INTAKE_URL = API_URL + "vba_documents/v1/"


def create_path_to_upload_file():
    """Creates a path to upload a file.
    Returns
    -------
    r : json
        Response in json format.
    """
    retries = 0
    ref_url = BENEFITS_INTAKE_URL + "uploads"
    try:
        r = requests.post(ref_url, headers=API_KEY_HEADER)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.error(f"Connection timeout, retry #{retries}")
            create_path_to_upload_file()
        else:
            logging.error(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)


def upload_file(params, files):
    """Upload a file for benefit intake.
    Parameters
    ----------
    params : dict
        The params to submit with the file upload.
    files: str
        Pointer to files.

    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + "path"
    retries = 0
    try:
        r = requests.put(params.get("location"), files=files)
        print(r.request.headers)
        print(r.request.body)
        r.raise_for_status()
        if r.status_code == 200:
            return r
        else:
            logging.error(f"Invalid Response status code of {r.status_code}")
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.error(f"Connection timeout, retry #{retries}")
            upload_file(params)
        else:
            logging.error(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)


def bulk_status_report():
    """Retrieves a bulk status report of all reports uploaded.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + "uploads/report"
    r = requests.post(ref_url, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()


def get_uploaded_document(doc_id):
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
    r = requests.get(ref_url, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()


def download_uploaded_document(doc_id):
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
    r = requests.get(ref_url, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()
