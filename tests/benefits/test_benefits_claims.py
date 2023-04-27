import json
import unittest
from requests import Session
from pyvet import creds
from pyvet.benefits.claims.api import (
    get_claims,
    get_claim,
    submit_526,
    upload_526,
    upload_supporting_doc_526,
    submit_intent_to_file,
    get_last_active_intent_to_file,
)
from unittest.mock import ANY, patch, mock_open


mock_headers = (
    dict(
        apiKey=creds.API_KEY_HEADER.get("apiKey"),
        # Authorization=creds.API_KEY_HEADER.get(
        #     "Authorization", "Bearer somerandomtoken"
        # ),
    ),
)

mock_claims = {
    "data": [
        {
            "id": "600106271",
            "type": "evss_claims",
            "attributes": {
                "evss_id": 600106271,
                "date_filed": "2017-07-06",
                "min_est_date": None,
                "max_est_date": None,
                "open": False,
                "waiver_submitted": False,
                "documents_needed": False,
                "development_letter_sent": False,
                "decision_letter_sent": False,
                "requested_decision": False,
                "claim_type": "Dependency",
                "status": "Complete",
            },
        }
    ]
}

mock_claim = {
    "data": {
        "id": "cb798e60-4b61-4f7b-b8d2-d04777df0fb1",
        "type": "claims_api_claim",
        "attributes": {
            "evss_id": 600118851,
            "date_filed": "2017-12-08",
            "min_est_date": None,
            "max_est_date": None,
            "open": True,
            "waiver_submitted": False,
            "documents_needed": False,
            "development_letter_sent": False,
            "decision_letter_sent": False,
            "requested_decision": False,
            "claim_type": "Compensation",
            "contention_list": ["abscess kidney (New)"],
            "va_representative": "DALE M BOETTCHER",
            "events_timeline": [
                {
                    "tracked_item_id": None,
                    "file_type": "Medical Treatment Records - Furnished by SSA",
                    "document_type": "L478",
                    "filename": "VickiSchmidt_PINT_b4_add_update.pdf",
                    "upload_date": "2017-12-08",
                    "type": "other_documents_list",
                    "date": "2017-12-08",
                },
                {
                    "tracked_item_id": None,
                    "file_type": "VA 21-526EZ, Fully Developed Claim (Compensation)",
                    "document_type": "L533",
                    "filename": "WESLEY_FORD_526.pdf",
                    "upload_date": "2017-12-08",
                    "type": "other_documents_list",
                    "date": "2017-12-08",
                },
                {"type": "phase1", "date": "2017-12-08"},
                {"type": "filed", "date": "2017-12-08"},
            ],
            "status": "Initial review",
            "supporting_documents": [
                {
                    "id": "80b6f78c-c4c1-4964-b64f-9dcaae29cd57",
                    "type": "claim_supporting_document",
                    "md5": "d927c7e283b3158a54822a493d06181d",  # pragma: allowlist secret
                    "filename": "extras.pdf",
                    "uploaded_at": "2023-02-15T21:08:36.076Z",
                }
            ],
        },
    }
}


class TestBenefitsClaims(unittest.TestCase):
    def setUp(self):
        self.headers = mock_headers
        self.benefits_claims_url = creds.VA_SANDBOX_API + "claims/v1/"

    @patch("pyvet.client.get_bearer_token", return_value="somerandomtoken")
    @patch.object(Session, "get", headers=mock_headers)
    def test_get_claims(self, mock_get, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_claims
        assert mock_get.headers == self.headers
        some_veteran_claims = get_claims(
            ssn="796130115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
        )
        mock_token.assert_called_once()
        self.assertDictEqual(
            some_veteran_claims,
            mock_claims,
        )
        mock_get.assert_called_once_with(
            self.benefits_intake_url + "claims",
        )

    @patch("pyvet.client.get_bearer_token", return_value="somerandomtoken")
    @patch.object(Session, "get", headers=mock_headers)
    def test_get_claim(self, mock_get, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_claim
        assert mock_get.headers == self.headers
        some_veteran_claim = get_claim(
            claim_id="600106271",
            ssn="796130115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
        )
        mock_token.assert_called_once()
        self.assertDictEqual(
            some_veteran_claim,
            mock_claim,
        )
        mock_get.assert_called_once_with(
            self.benefits_intake_url + f"claims/{600106271}",
        )


if __name__ == "__main__":
    unittest.main()
