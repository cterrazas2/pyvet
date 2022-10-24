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

VA_PROD_API = os.getenv("VA_PROD_API", "https://api.va.gov/services/")
VA_SANDBOX_API = os.getenv("VA_SANDBOX_API", "https://sandbox-api.va.gov/services/")

CLIENT_ID = os.getenv("VA_CLIENT_ID", "REPLACE ME")
CLIENT_SECRET = os.getenv("VA_CLIENT_SECRET", "REPLACE ME")

API_KEY = os.getenv("VA_API_KEY", "REPLACE ME")
API_KEY_HEADER = dict(apiKey=API_KEY)
API_URL = VA_SANDBOX_API if DEV else VA_PROD_API
