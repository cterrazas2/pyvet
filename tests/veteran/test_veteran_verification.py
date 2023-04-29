import unittest
from pyvet import creds
from pyvet.veteran.verification.api import (
    get_status,
    get_disability_rating,
    get_service_history,
)
from requests import Session

from unittest.mock import patch

mock_confirmed = dict(veteran_status="confirmed")

mock_disability_rating = {
    "data": {
        "id": "12303",
        "type": "disability-rating",
        "attributes": {
            "combined_disability_rating": 100,
            "combined_effective_date": "2018-03-27",
            "legal_effective_date": "2018-03-27",
            "individual_ratings": [
                {
                    "decision": "Service Connected",
                    "effective_date": "2018-03-27",
                    "rating_percentage": 50,
                }
            ],
        },
    }
}

mock_service_history = {
    "data": [
        {
            "id": "12312AASDf",
            "type": "service-history-episodes",
            "attributes": {
                "first_name": "Abraham",
                "last_name": "Lincoln",
                "start_date": "1948-04-08",
                "end_date": "1950-05-10",
                "branch_of_service": "Air Force",
                "pay_grade": "W01",
                "discharge_status": "honorable",
                "separation_reason": "SUFFICIENT SERVICE FOR RETIREMENT",
                "deployments": [
                    {
                        "start_date": "1948-10-10",
                        "end_date": "1949-10-09",
                        "location": "KOR",
                    }
                ],
            },
        }
    ]
}


@patch(
    "pyvet.veteran.verification.api.get_bearer_token",
    return_value="somerandomtoken",
)
@patch.object(Session().headers, "get", return_value=None)
@patch.object(
    Session,
    "get",
    headers=dict(
        apiKey=creds.API_KEY_HEADER.get("apiKey"),
        Authorization=creds.API_KEY_HEADER.get(
            "Authorization", "Bearer somerandomtoken"
        ),
    ),
)
class TestVeteranVerification(unittest.TestCase):
    def setUp(self):
        self.headers = creds.API_KEY_HEADER
        self.headers["Authorization"] = "Bearer somerandomtoken"
        self.verification_url = creds.VA_SANDBOX_API + "veteran_verification/v1/"
        creds.API_KEY_HEADER["Authorization"] = None

    def test_get_status(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_confirmed
        assert mock_auth.return_value == None
        vet_status = get_status()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(vet_status, mock_confirmed)
        mock_get.assert_called_once_with(
            self.verification_url + "status", headers=self.headers
        )

    def test_disability_rating(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_disability_rating
        assert mock_auth.return_value == None
        disability_rating = get_disability_rating()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(disability_rating, mock_disability_rating)
        mock_get.assert_called_once_with(
            self.verification_url + "disability_rating", headers=self.headers
        )

    def test_service_history(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_service_history
        assert mock_auth.return_value == None
        service_history = get_service_history()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        print(f"mock_get.headers: {mock_get.headers}")
        assert mock_get.headers == self.headers
        self.assertDictEqual(service_history, mock_service_history)
        mock_get.assert_called_once_with(
            self.verification_url + "service_history", headers=self.headers
        )


if __name__ == "__main__":
    unittest.main()
