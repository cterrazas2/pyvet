####################
# VA CREDS         #
####################
from collections.abc import MutableMapping
import os

DEV: bool = os.getenv("DEV", "True").lower() in (
    "true",
    "t",
    "1",
)
PROD: bool = os.getenv("PROD", "False").lower() in (
    "true",
    "t",
    "1",
)

VA_PROD_API: str = "https://api.va.gov/services/"
VA_SANDBOX_API: str = "https://sandbox-api.va.gov/services/"

CLIENT_ID: str = os.getenv("VA_CLIENT_ID", "REPLACE ME")
CLIENT_SECRET: str = os.getenv("VA_CLIENT_SECRET", "REPLACE ME")
CLIENT_ASSERTION: str = os.getenv("VA_CLIENT_ASSERTION", "REPLACE ME")

API_KEY: str = os.getenv("VA_API_KEY", "REPLACE ME")
API_KEY_HEADER: MutableMapping[str, str | bytes] = dict(apiKey=API_KEY)
API_URL: str = VA_SANDBOX_API if DEV else VA_PROD_API

API_RETRIES: int = 5
API_BACKOFF_FACTOR: float = 0.3
API_FORCE_LIST: tuple[int, int, int] = (500, 502, 504)

####################
# VA AUTH INFO     #
####################
AUTH_SERVER: str = "https://sandbox-api.va.gov/oauth2"
# ISSUER = "https://sandbox-api.va.gov" # below is issuer from VA's '.well-known/openid-configuration' file
ISSUER: str = "https://deptva-eval.okta.com/oauth2/default"
REDIRECT: str = "http://127.0.0.1:39303/oauth2/callback"
DEFAULT_SCOPE: str = "profile openid offline_access"
