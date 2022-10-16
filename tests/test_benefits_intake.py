import unittest
from pyvet import creds
from pyvet.benefits_intake.api import create_path_to_upload_file, upload_file
from unittest.mock import patch

mock_create_path = dict(
    data=dict(
        id="6d8433c1-cd55-4c24-affd-f592287a7572",
        type="document_upload",
        attributes=dict(
            guid="6d8433c1-cd55-4c24-affd-f592287a7572",
            status="pending",
            code="string",
            detail="string",
            location="https://sandbox-api.va.gov/services_user_content/vba_documents/some-random-id",
            updated_at="2018-07-30T17:31:15.958Z",
            uploaded_pdf=None,
        ),
    )
)


class TestBenefitsIntake(unittest.TestCase):
    def setUp(self):
        self.headers = creds.API_KEY_HEADER
        self.benefits_intake_url = creds.VA_SANDBOX_API + "vba_documents/v1/"

    @patch("pyvet.benefits_intake.api.requests.post")
    def test_create_path_to_upload_files(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_create_path
        resp = create_path_to_upload_file()
        self.assertDictEqual(resp, mock_create_path)
        mock_post.assert_called_once_with(
            self.benefits_intake_url + "uploads", headers=self.headers
        )

    @patch("pyvet.benefits_intake.api.requests.put")
    def test_upload_file(self, mock_put):
        mock_put.return_value.status_code = 200
        mock_files = (
            ("file_1", (None, "text")),
            ("file_2", (None, "more text")),
            ("file_3", (None, "and more text")),
        )
        mock_params = dict(
            guid="6d8433c1-cd55-4c24-affd-f592287a7572",
            status="pending",
            code="string",
            detail="string",
            location="https://sandbox-api.va.gov/services_user_content/vba_documents/some-random-id",
            updated_at="2018-07-30T17:31:15.958Z",
            uploaded_pdf="null",
        )
        upload_url = mock_params.get("location")
        upload_file(params=mock_params, files=mock_files)
        mock_put.assert_called_once_with(
            upload_url,
            files=mock_files,
        )


if __name__ == "__main__":
    unittest.main()
