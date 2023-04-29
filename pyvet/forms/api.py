"""
Forms API: https://developer.va.gov/explore/vaForms/docs/vaForms?version=current
"""
import json
import logging
import requests

from pyvet.creds import API_URL
from pyvet.client import current_session as session
from pyvet.json_alias import Json

FORMS_URL = API_URL + "va_forms/v0/forms"


def get_forms(query: str | None = None) -> Json:
    """Gets all forms with optional params.
    Parameters
    ----------
    query : str
        The query to search for.
    Returns
    -------
    r : json
        Response in json format.
    """
    try:
        r = session.get(FORMS_URL, params=dict(query=query))
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_form(form_name: str) -> Json:
    """Gets a form by name.
    Parameters
    ----------
    form_name : str
        The name of the form.
    Returns
    -------
    r : json
        Response in json format.
    """
    form_url = FORMS_URL + "/" + form_name
    try:
        r = session.get(form_url, params=dict(form_name=form_name))
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)
