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
    get_poa_status_by_id,
    get_status_poa_last_active,
)
from tests.data.mock_benefits_claims import (
    MOCK_CLAIM,
    MOCK_CLAIMS,
    MOCK_INTENT_TO_FILE,
    MOCK_INTENT_TO_FILE_LAST_ACTIVE,
    MOCK_POA_STATUS_ID,
    MOCK_POA_LAST_ACTIVE,
)
from unittest.mock import patch


mock_headers = dict(apiKey=creds.API_KEY_HEADER.get("apiKey"))


class TestBenefitsClaims(unittest.TestCase):
    def setUp(self):
        self.headers = dict(
            apiKey=creds.API_KEY_HEADER.get("apiKey"),
            Authorization="Bearer somerandomtoken",
        )
        self.benefits_claims_url = creds.VA_SANDBOX_API + "claims/v1/"
        creds.API_KEY_HEADER["Authorization"] = None

    @patch(
        "pyvet.benefits.claims.api.get_bearer_token",
        return_value="somerandomtoken",
    )
    @patch.object(Session().headers, "get", return_value=None)
    @patch.object(
        Session, "get", headers=dict(apiKey=creds.API_KEY_HEADER.get("apiKey"))
    )
    def test_get_claims(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_CLAIMS
        assert mock_auth.return_value == None
        some_veteran_claims = get_claims(
            ssn="796130115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
        )
        assert mock_get.headers == mock_headers
        mock_token.assert_called_once()
        self.assertDictEqual(
            some_veteran_claims,
            MOCK_CLAIMS,
        )
        mock_get.assert_called_once_with(
            self.benefits_claims_url + "claims",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )
        creds.API_KEY_HEADER["Authorization"] = None

    @patch(
        "pyvet.benefits.claims.api.get_bearer_token",
        return_value="somerandomtoken",
    )
    @patch.object(Session().headers, "get", return_value=None)
    @patch.object(
        Session, "get", headers=dict(apiKey=creds.API_KEY_HEADER.get("apiKey"))
    )
    def test_get_claim(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_CLAIM
        assert mock_auth.return_value == None
        some_veteran_claim = get_claim(
            claim_id="600106271",
            ssn="796130115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
        )
        assert mock_get.headers == mock_headers
        mock_token.assert_called_once()
        self.assertDictEqual(
            some_veteran_claim,
            MOCK_CLAIM,
        )
        mock_get.assert_called_once_with(
            self.benefits_claims_url + f"claims/{600106271}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    @patch(
        "pyvet.benefits.claims.api.get_bearer_token",
        return_value="somerandomtoken",
    )
    @patch.object(Session().headers, "get", return_value=None)
    @patch.object(
        Session, "post", headers=dict(apiKey=creds.API_KEY_HEADER.get("apiKey"))
    )
    def test_submit_intent_to_file(self, mock_post, mock_auth, mock_token):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = MOCK_INTENT_TO_FILE
        assert mock_auth.return_value == None
        intent = submit_intent_to_file(
            is_representative=False,
            ssn="796130115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
        )
        print(intent)
        assert mock_post.headers == mock_headers
        mock_token.assert_called_once()
        self.assertDictEqual(
            intent,
            MOCK_INTENT_TO_FILE,
        )
        mock_post.assert_called_once_with(
            self.benefits_claims_url + "forms/0966",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            data={"type": "form/0966", "attributes": {"type": "compensation"}},
        )

    @patch(
        "pyvet.benefits.claims.api.get_bearer_token",
        return_value="somerandomtoken",
    )
    @patch.object(Session().headers, "get", return_value=None)
    @patch.object(
        Session, "get", headers=dict(apiKey=creds.API_KEY_HEADER.get("apiKey"))
    )
    def test_get_last_active_intent_to_file(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_INTENT_TO_FILE_LAST_ACTIVE
        assert mock_auth.return_value == None
        last_active_intent = get_last_active_intent_to_file(
            is_representative=False,
            intent_type="compensation",
            ssn="796130115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
        )
        assert mock_get.headers == mock_headers
        mock_token.assert_called_once()
        self.assertDictEqual(
            last_active_intent,
            MOCK_INTENT_TO_FILE_LAST_ACTIVE,
        )
        mock_get.assert_called_once_with(
            self.benefits_claims_url + f"forms/0966/active",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={"type": "compensation"},
        )

    @patch(
        "pyvet.benefits.claims.api.get_bearer_token",
        return_value="somerandomtoken",
    )
    @patch.object(Session().headers, "get", return_value=None)
    @patch.object(
        Session, "get", headers=dict(apiKey=creds.API_KEY_HEADER.get("apiKey"))
    )
    def test_get_poa_status_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_POA_STATUS_ID
        assert mock_auth.return_value == None
        poa_status = get_poa_status_by_id(
            poa_id="05b41b80-9990-4e0c-86f1-44db8bca2225",
            is_representative=False,
            ssn="796130115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
        )
        assert mock_get.headers == mock_headers
        mock_token.assert_called_once()
        self.assertDictEqual(
            poa_status,
            MOCK_POA_STATUS_ID,
        )
        mock_get.assert_called_once_with(
            self.benefits_claims_url
            + "forms/2122/05b41b80-9990-4e0c-86f1-44db8bca2225",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    @patch(
        "pyvet.benefits.claims.api.get_bearer_token",
        return_value="somerandomtoken",
    )
    @patch.object(Session().headers, "get", return_value=None)
    @patch.object(
        Session, "get", headers=dict(apiKey=creds.API_KEY_HEADER.get("apiKey"))
    )
    def test_status_poa_last_active(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_POA_LAST_ACTIVE
        assert mock_auth.return_value == None
        poa_status = get_status_poa_last_active(
            is_representative=False,
            ssn="796130115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
        )
        assert mock_get.headers == mock_headers
        mock_token.assert_called_once()
        self.assertDictEqual(
            poa_status,
            MOCK_POA_LAST_ACTIVE,
        )
        mock_get.assert_called_once_with(
            self.benefits_claims_url + "forms/2122/active",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )


if __name__ == "__main__":
    unittest.main()
