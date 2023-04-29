####################
# VA CREDS         #
####################
import os

DEV = os.getenv("DEV", "True").lower() in (
    "true",
    "t",
    "1",
)
PROD = os.getenv("PROD", "False").lower() in (
    "true",
    "t",
    "1",
)

VA_PROD_API = "https://api.va.gov/services/"
VA_SANDBOX_API = "https://sandbox-api.va.gov/services/"

CLIENT_ID = os.getenv("VA_CLIENT_ID", "REPLACE ME")
CLIENT_SECRET = os.getenv("VA_CLIENT_SECRET", "REPLACE ME")
CLIENT_ASSERTION = os.getenv("VA_CLIENT_ASSERTION", "REPLACE ME")

API_KEY = os.getenv("VA_API_KEY", "REPLACE ME")
API_KEY_HEADER = dict(apiKey=API_KEY)
API_URL = VA_SANDBOX_API if DEV else VA_PROD_API

API_RETRIES = 5
API_BACKOFF_FACTOR = 0.3
API_FORCE_LIST = (500, 502, 504)

####################
# VA AUTH INFO     #
####################
AUTH_SERVER = "https://sandbox-api.va.gov/oauth2"
# ISSUER = "https://sandbox-api.va.gov" # below is issuer from VA's '.well-known/openid-configuration' file
ISSUER = "https://deptva-eval.okta.com/oauth2/default"
REDIRECT = "http://127.0.0.1:39303/oauth2/callback"
DEFAULT_SCOPE = "profile openid offline_access"
