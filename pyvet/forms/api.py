"""
Forms API: https://developer.va.gov/explore/vaForms/docs/vaForms?version=current
"""

from pyvet.client import current_session as session
from pyvet.client import session_call
from pyvet.creds import API_URL
from pyvet.json_alias import Json

FORMS_URL = API_URL + "va_forms/v0/forms"


@session_call()
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
    return session.get(FORMS_URL, params={"query": query})


@session_call()
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
    return session.get(form_url, params={"form_name": form_name})
