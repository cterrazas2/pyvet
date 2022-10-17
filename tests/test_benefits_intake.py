import unittest
from pyvet import creds
from pyvet.benefits_intake.api import (
    create_path_to_upload_file,
    upload_file,
    bulk_status_report,
    get_uploaded_document,
    download_uploaded_document,
)
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

mock_bulk = dict(
    data=[
        dict(
            attributes=dict(
                code="DOC105",
                detail="Invalid or unknown id",
                guid="6d8433c1-cd55-4c24-affd-f592287a7572",
                location=None,
                status="error",
                updated_at=None,
                uploaded_pdf=None,
            ),
            id="6d8433c1-cd55-4c24-affd-f592287a7572",
            type="document_upload",
        )
    ]
)

mock_doc = dict(
    data=dict(
        id="6d8433c1-cd55-4c24-affd-f592287a7572",
        type="document_upload",
        attributes=dict(
            guid="6d8433c1-cd55-4c24-affd-f592287a7572",
            status="received",
            code="string",
            message="string",
            detail="string",
            updated_at="2018-07-30T17:31:15.958Z",
            uploaded_pdf=dict(
                total_documents=2,
                total_pages=3,
                content=dict(
                    page_count=1,
                    dimensions=dict(
                        height=11,
                        width=8.5,
                        oversized_pdf=False,
                    ),
                    attachments=[
                        dict(
                            page_count=2,
                            dimensions=dict(height=11, width=8.5, oversized_pdf=False),
                        )
                    ],
                ),
            ),
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

    @patch("pyvet.benefits_intake.api.requests.post")
    def test_bulk_status_report(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_bulk
        mock_guids = ["6d8433c1-cd55-4c24-affd-f592287a7572"]
        bulk = bulk_status_report(guids=mock_guids)
        self.assertDictEqual(bulk, mock_bulk)
        mock_post.assert_called_once_with(
            self.benefits_intake_url + "uploads/report",
            json=dict(ids=mock_guids),
            headers=self.headers,
        )

    @patch("pyvet.benefits_intake.api.requests.get")
    def test_upload_document(self, mock_get):
        self.maxDiff = None
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_doc
        mock_file_guid = "6d8433c1-cd55-4c24-affd-f592287a7572"
        doc = get_uploaded_document(doc_id=mock_file_guid)
        self.assertDictEqual(doc, mock_doc)
        mock_get.assert_called_once_with(
            self.benefits_intake_url + f"uploads/{mock_file_guid}",
            headers=self.headers,
        )

    @patch("pyvet.benefits_intake.api.requests.get")
    def test_download_uploaded_document(self, mock_get):
        self.maxDiff = None
        mock_get.return_value.status_code = 200
        mock_file_guid = "6d8433c1-cd55-4c24-affd-f592287a7572"
        download_uploaded_document(doc_id=mock_file_guid)
        mock_get.assert_called_once_with(
            self.benefits_intake_url + f"uploads/{mock_file_guid}/download",
            headers=self.headers,
        )


if __name__ == "__main__":
    unittest.main()
