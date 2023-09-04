import unittest
from unittest.mock import patch

from requests import Session

from pyvet import creds
from pyvet.health.community_care.api import get_eligibility

mock_community_care = {
    "patientRequest": {
        "patientIcn": "011235813V213455",
        "serviceType": "PrimaryCare",
        "timestamp": "2019-05-09T13:17:58.250Z",
    },
    "eligibilityCodes": [{"description": "Basic", "code": "B"}],
    "grandfathered": False,
    "noFullServiceVaMedicalFacility": False,
    "patientAddress": {
        "country": "USA",
        "street": "742 Evergeen Terrace",
        "city": "Springfield",
        "state": "KY",
        "zip": "89144",
    },
    "patientCoordinates": {"latitude": 40.758541, "longitude": -73.982132},
    "nearbyFacilities": [
        {
            "id": "vha_1597XY",
            "name": "Springfield VA Clinic",
            "physicalAddress": {
                "street": "2584 South Street",
                "city": "Springfield",
                "state": "KY",
                "zip": "10946",
            },
            "coordinates": {"latitude": 41.81, "longitude": 67.65},
            "driveMinutes": {"min": 0, "max": 10},
            "phoneNumber": "177-112-8657 x",
            "website": "https://www.va.gov",
        },
        {
            "id": "vha_46368ZZ",
            "name": "Shelbyville VA Clinic",
            "physicalAddress": {
                "street": "121393 Main Street",
                "city": "Shelbyville",
                "state": "KY",
                "zip": "75025",
            },
            "coordinates": {"latitude": 196.418, "longitude": 317.811},
            "driveMinutes": {"min": 20, "max": 30},
            "phoneNumber": "1-422-983-2040",
            "website": "https://www.va.gov",
            "mobile": False,
            "active": True,
        },
    ],
    "eligible": False,
    "processingStatus": "successful",
    "pactStatus": "Active",
    "$lock": [],
}


@patch(
    "pyvet.health.community_care.api.token_scheduler.get_bearer_token",
    return_value="somerandomtoken",
)
@patch.object(Session().headers, "get", return_value=None)
@patch.object(Session, "get", headers={"apiKey": creds.API_KEY_HEADER.get("apiKey")})
class TestHealthCommunityCare(unittest.TestCase):
    def setUp(self):
        self.headers = {"apiKey": creds.API_KEY_HEADER.get("apiKey")}
        self.health_url = creds.VA_SANDBOX_API + "community-care/v0/eligibility/"
        creds.API_KEY_HEADER["Authorization"] = None

    def test_get_eligibility(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_community_care
        assert mock_auth.return_value == None
        eligibility = get_eligibility(patient="32000225", service_type="Dermatology")
        mock_token.assert_called_once()
        assert mock_get.headers == self.headers
        self.assertDictEqual(eligibility, mock_community_care)
        mock_get.assert_called_once_with(
            self.health_url + "search",
            headers={
                "apiKey": creds.API_KEY_HEADER.get("apiKey"),
                "Authorization": "Bearer somerandomtoken",
            },
            params={
                "patient": "32000225",
                "serviceType": "Dermatology",
                "extendedDriveMin": None,
            },
        )


if __name__ == "__main__":
    unittest.main()
