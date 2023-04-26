"""
Benefits Intake API: https://developer.va.gov/explore/benefits/docs/claims?version=v1
Note: V1 is for external users, V2 is for internal users.
"""
import json
import logging
import os
import pathlib
import requests
from pyvet.client import (
    current_session as session,
    get_bearer_token,
)
from pyvet.creds import API_URL

BENEFITS_INTAKE_URL = API_URL + "claims/v1/"
CLAIM_SCOPE = "openid profile offline_access claim.read claim.write"
# "openid", "profile" "offline_access" , "claim.read", "claim.write"


def get_claims(
    is_representative: bool = False,
    ssn: str = None,
    first_name: str = None,
    last_name: str = None,
    birth_date: str = None,
):
    """Get claims for a veteran.
    Parameters
    ----------
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="claims", scope=CLAIM_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    if is_representative:
        session.headers["X-VA-SSN"] = ssn
        session.headers["X-VA-First-Name"] = first_name
        session.headers["X-VA-Last-Name"] = last_name
        session.headers["X-VA-Birth-Date"] = birth_date

    claims_url = BENEFITS_INTAKE_URL + f"claims"
    try:
        r = session.get(claims_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_claim(
    claim_id: str,
    is_representative: bool = False,
    ssn: str = None,
    first_name: str = None,
    last_name: str = None,
    birth_date: str = None,
):
    """Get claim details.
    Parameters
    ----------
    claim_id : str
        The claim id.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    claim_url = BENEFITS_INTAKE_URL + f"claims/{claim_id}"
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="claims", scope=CLAIM_SCOPE)
        if token is None:
            logging.error("Fetcing token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    if is_representative:
        session.headers["X-VA-SSN"] = ssn
        session.headers["X-VA-First-Name"] = first_name
        session.headers["X-VA-Last-Name"] = last_name
        session.headers["X-VA-Birth-Date"] = birth_date
    try:
        r = session.get(claim_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def submit_526(
    is_first_claim: bool = False,
    is_representative: bool = False,
    ssn: str = None,
    first_name: str = None,
    last_name: str = None,
    birth_date: str = None,
):
    """Submit a 526 claim.
    Parameters
    ----------
    is_first_claim : bool
        If this is the veteran's first claim.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    submission_url = BENEFITS_INTAKE_URL + f"forms/526"
    token = get_bearer_token(va_api="claims", scope=CLAIM_SCOPE)
    if session.headers.get("Authorization") is None:
        session.headers["Authorization"] = f"Bearer {token}"

    if is_representative:
        session.headers["X-VA-SSN"] = ssn
        session.headers["X-VA-First-Name"] = first_name
        session.headers["X-VA-Last-Name"] = last_name
        session.headers["X-VA-Birth-Date"] = birth_date

    try:
        r.session.post(
            submission_url,
            headers=session.headers,
            files={"form526": open("form526.pdf", "rb")},
        )
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def upload_526(
    doc_id: str,
    is_representative: bool = False,
    ssn: str = None,
    first_name: str = None,
    last_name: str = None,
    birth_date: str = None,
):
    """Upload a 526 claim.
    Parameters
    ----------
    doc_id : str
        The document id.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    pass


def upload_supporting_doc_526(
    doc_id: str,
    is_representative: bool = False,
    ssn: str = None,
    first_name: str = None,
    last_name: str = None,
    birth_date: str = None,
):
    """Upload a supporting document for a 526 claim.
    Parameters
    ----------
    doc_id : str
        The document id.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    pass


def submit_intent_to_file(
    is_representative: bool = False,
    ssn: str = None,
    first_name: str = None,
    last_name: str = None,
    birth_date: str = None,
):
    """Submit an intent to file for disability compensation, burial, or pension claims.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    pass


def get_last_active_intent_to_file(
    is_representative: bool = False,
    ssn: str = None,
    first_name: str = None,
    last_name: str = None,
    birth_date: str = None,
):
    """Get the last active intent to file for disability compensation, burial, or pension claims.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    pass
