"""
Benefits API: https://developer.va.gov/explore/benefits/docs/claims?version=current
"""
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

CLAIMS_URL = API_URL + "claims/v1"


def get_claims(ssn, fn, ln):
    """
    Parameters
    ----------
    ssn : str
        Veteran's ssn to submit for claims.
    fn : str
        First name of veteran.
    ln : str
        Last name of veteran.

    Returns
    -------

    """
    payload = {"X-VA-SSN": ssn, "X-VA-First-Name": fn, "X-VA-Last-Name": ln}
    claims_url = CLAIMS_URL + "/claims"
    return requests.get(claims_url, params=payload)


def get_claim(vet_id, ssn, fn, ln):
    """Gets a claim for a veteran by an id, with required params.
    Parameters
    ----------
    vet_id : str
        Veteran id for claim.
    ssn : str
        Veteran's ssn for claim.
    fn : str
        Veteran's first name.
    ln : str
        Veteran's last name.
    Returns
    -------
    """
    payload = {
        "id": vet_id,
        "X-VA-SSN": ssn,
        "X-VA-First-Name": fn,
        "X-VA-Last-Name": ln,
    }
    claim_url = CLAIMS_URL + "/claims/" + vet_id
    return requests.get(claim_url, params=payload)


def submit_claim(ssn, fn, ln, bd):
    """Submits a claim for a veteran with required params.
    Parameters
    ----------
    ssn : str
        Veteran's ssn for claim.
    fn : str
        Veteran's first name.
    ln : str
        Veteran's last name.
    bd : str
        Veteran's birthdate.
    Returns
    -------

    """
    payload = {
        "X-VA-SSN": ssn,
        "X-VA-First-Name": fn,
        "X-VA-Last-Name": ln,
        "X-VA-Birth-Date": bd,
    }
    data = {
        "type": "form/526",
        "attributes": {"veteran": {"currentlyVAEmployee": "false"}},
    }
    claim_url = CLAIMS_URL + "/forms/526"
    return requests.post(claim_url, params=payload, data=data)


def upload_to_claim(claim_id, ssn, fn, ln, bd):
    """Uploads data_json to a veteran's claim by a claim id, with required params.
    Parameters
    ----------
    claim_id : str
        ID of claim.
    ssn : str
        Veteran's ssn for claim.
    fn : str
        Veteran's first name.
    ln : str
        Veteran's last name.
    bd : str
        Veteran's birthdate.

    Returns
    -------

    """
    payload = {
        "id": claim_id,
        "X-VA-SSN": ssn,
        "X-VA-First-Name": fn,
        "X-VA-Last-Name": ln,
        "X-VA-Birth-Date": bd,
    }
    data = {"data_json": {"id": claim_id, "type": "claims_api_claim", "attributes": {}}}
    claim_url = CLAIMS_URL + "/forms/526/"
    return requests.put(claim_url, params=payload, data=data)


def get_disabilities():
    """Returns all VA disabilities.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = API_URL + "benefits-reference-data_json/v1/disabilities"
    r = requests.get(ref_url, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()
