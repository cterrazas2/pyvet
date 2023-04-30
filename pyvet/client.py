import logging
import requests

# the below is an internal version, with some modifications. It is not the same as the one in the pyvet package.
import pyvet.oidc_client as oidc

# import oidc_client as oidc
from pyvet.creds import (
    API_BACKOFF_FACTOR,
    API_FORCE_LIST,
    API_KEY_HEADER,
    API_RETRIES,
    AUTH_SERVER,
    CLIENT_ID,
    CLIENT_SECRET,
    DEFAULT_SCOPE,
    ISSUER,
    REDIRECT,
)
from dataclasses import dataclass
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

"""
scopes:


profile openid offline_access

claim.read claim.write

fhirUser launch patient/Condition.read patient/MedicationDispense.read patient/MedicationRequest.read patient/Observation.read patient/Patient.read patient/Practitioner.read

launch/patient patient/CommunityCareEligibility.read

launch/patient patient/AllergyIntolerance.read patient/Appointment.read patient/Binary.read patient/Condition.read patient/Device.read patient/DeviceRequest.read patient/DiagnosticReport.read patient/DocumentReference.read patient/Encounter.read patient/Immunization.read patient/Location.read patient/Medication.read patient/MedicationOrder.read patient/MedicationRequest.read patient/MedicationStatement.read patient/Observation.read patient/Organization.read patient/Patient.read patient/Practitioner.read patient/PractitionerRole.read patient/Procedure.read

disability_rating.read service_history.read veteran_status.read


"""


def get_bearer_token(va_api: str, scope: str = DEFAULT_SCOPE) -> str | None:
    """Get a bearer token from the VA OIDC server.
    Parameters
    ----------
    va_api : str
        The VA API to request a token for.
    scope : str
        A scope to request from the VA OIDC server (different per VA API).
    Returns
    -------
    token : str
        A bearer token.
    """
    try:
        """
        Update 04/29:
        So, I looked in the va's '.well-known/openid-configuration' file and it indeed has the below routes:
           authorization_endpoint: https://sandbox-api.va.gov/oauth2/authorization
           token_endpoint: https://sandbox-api.va.gov/oauth2/token

        this doesn't work?:
        token_endpoint=f"https://sandbox-api.va.gov/oauth2/token",

        this works:
        authorization_endpoint=f"https://sandbox-api.va.gov/oauth2/authorization",

        Neither of below is working (shown in va docs)?:
            token_endpoint=f"https://sandbox-api.va.gov/oauth2/{va_api}/v1/token",
            authorization_endpoint=f"https://sandbox-api.va.gov/oauth2/{va_api}/v1/authorization",
        """
        va_api_version = f"{va_api}/v1"
        token = oidc.login(
            provider_config=oidc.config.ProviderConfig(
                issuer=ISSUER,
                authorization_endpoint=f"{AUTH_SERVER}/authorization",
                token_endpoint=f"{AUTH_SERVER}/token",
            ),
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT,  # update this later
            scope=scope,
            interactive=True,
        )
        return token.access_token
    except Exception as e:
        logging.error(e)


# @dataclass(frozen=True)
# class RequestSession:
#     """A session object with the VA API key."""

#     session: requests.Session
#     token: oidc.TokenResponse = None


def create_session() -> requests.Session:
    """Create a session with the VA API.
    Returns
    -------
    session : requests.Session:
        A session object with the VA API key.
    """
    session = requests.Session()
    session.headers = API_KEY_HEADER
    retry = Retry(
        total=API_RETRIES,
        read=API_RETRIES,
        connect=API_RETRIES,
        backoff_factor=API_BACKOFF_FACTOR,
        status_forcelist=API_FORCE_LIST,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


current_session = create_session()

if current_session.headers.get("apiKey") == "REPLACE ME":
    logging.error(
        "No API key set, visit: https://developer.va.gov/onboarding/request-sandbox-access"
    )
