"""
Benefits Intake API: https://developer.va.gov/explore/benefits/docs/benefits?version=current
"""
import json
import logging
import os
import pathlib
import requests
from pyvet.client import current_session as session
from pyvet.creds import API_URL

BENEFITS_INTAKE_URL = API_URL + "vba_documents/v1/"


def create_path_to_upload_files():
    """Creates a path to upload files.
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


def upload_files(params: dict, uploads_dir: str = "uploads", metadata: dict = None):
    """Uploads file(s) to the benefit intake api.
    Parameters
    ----------
    params : dict
        The params to extract the location to submit the file upload.
    uploads_dir: str
        The name of the directory for file uploads.
    metadata: dict
        A dict with optional file metadata.

    Returns
    -------
    r : Response
        A Response obejct from requests.

    Notes
    -------
    To upload files to the VA benefits intake api, files must contain any of the below fields (except metadata) and all naming must match exactly:
        metadata - a dict of file metadata
        content - main content file
        attachment1 - 1st attachment file
        attachmentN - Nth attachemnt file

    Currently, pyvet will look in the uploads_dir, defaults to `uploads/`, within the current working directory.
    You should ensure this directory exists and place all files you want to upload here. Below is an example file
    structure:

    uploads/
        attachments/
            attachment1.pdf
            attachemnt2.pdf
        main_content.pdf

    """

    uploads_dir = pathlib.Path().resolve().as_posix() + f"/{uploads_dir}/"
    attachments_dir = uploads_dir + "attachments/"

    if not os.path.isdir(uploads_dir):
        logging.error(f"{uploads_dir} does not exist.")
    if not os.path.isdir(attachments_dir):
        logging.error(f"{attachments_dir} does not exist.")

    files = {}

    # add any metadata
    if metadata:
        try:
            serialized_json = json.dumps(metadata)
            files["metadata"] = (None, f"{serialized_json};type=application/json")
        except Exception as e:
            logging.error(e)
    try:

        # upload the main content pdf
        try:
            for file in os.listdir(uploads_dir):
                if not os.path.isdir(file) and "attachments" not in file:
                    files["content"] = open(uploads_dir + file, "rb")
        except OSError as ose:
            logging.error(ose)

        # then upload all other attachment pdfs
        try:
            for i, file in enumerate(os.listdir(attachments_dir)):
                files[f"attachment{i+1}"] = open(attachments_dir + file, "rb")
        except OSError as ose:
            logging.error(ose)

        r = session.put(
            params.get("location"),
            files=files,
        )

        r.raise_for_status()
        if r.status_code == 200:
            return r
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
