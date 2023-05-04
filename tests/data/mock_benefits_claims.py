MOCK_CLAIMS = {
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

MOCK_CLAIM = {
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

MOCK_INTENT_TO_FILE_LAST_ACTIVE = {
    "data": {
        "id": "183042",
        "type": "intent_to_file",
        "attributes": {
            "creation_date": "2020-06-05T11:24:28.000-05:00",
            "expiration_date": "2021-06-05T11:24:28.000-05:00",
            "type": "compensation",
            "status": "active",
        },
    }
}

MOCK_POA_STATUS_ID = {
    "data": {
        "id": "05b41b80-9990-4e0c-86f1-44db8bca2225",
        "type": "claims_api_power_of_attorneys",
        "attributes": {
            "status": "submitted",
            "date_request_accepted": "2023-02-15",
            "representative": {"service_organization": {"poa_code": "074"}},
            "previous_poa": None,
        },
    }
}

MOCK_POA_LAST_ACTIVE = {
    "data": {
        "id": None,
        "type": "claims_api_power_of_attorneys",
        "attributes": {
            "status": "updated",
            "date_request_accepted": None,
            "representative": {
                "service_organization": {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "organization_name": None,
                    "phone_number": "555-555-5555",
                    "poa_code": "HelloWorld",
                }
            },
            "previous_poa": None,
        },
    }
}

MOCK_INTENT_TO_FILE = {
    "data": {
        "id": "184058",
        "type": "intent_to_file",
        "attributes": {
            "creation_date": "2020-08-10T08:31:26.000-05:00",
            "expiration_date": "2021-08-10T08:31:18.000-05:00",
            "type": "compensation",
            "status": "duplicate",
        },
    }
}
