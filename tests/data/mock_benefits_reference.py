MOCK_CONTENTION = {
    "items": [
        {"code": "INC", "description": "Increase"},
    ],
    "links": [
        {
            "href": "https://sandbox-api.va.gov/services/benefits-reference-data/v1/contention-types",
            "rel": "self",
        }
    ],
    "totalItems": 1,
    "totalPages": 1,
}

MOCK_TREATMENT_CENTERS = {
    "items": [
        {
            "city": "HONOLULU",
            "id": 12965766,
            "name": "VA PACIFIC ISLANDS HEALTH CARE SYSTEM",
            "state": "HI",
        },
    ],
    "links": [
        {
            "href": "https://sandbox-api.va.gov/services/benefits-reference-data/v1/treatment-centers",
            "rel": "self",
        }
    ],
    "totalItems": 1,
    "totalPages": 1,
}

MOCK_SERVICE_BRANCES = {
    "items": [
        {"code": "AF", "description": "Air Force"},
        {"code": "N ACAD", "description": "Naval Academy"},
        {"code": "CG", "description": "Coast Guard"},
        {"code": "MC", "description": "Marine Corps"},
        {"code": "AR", "description": "Army Reserves"},
    ],
    "links": [
        {
            "href": "https://sandbox-api.va.gov/services/benefits-reference-data/v1/service-branches",
            "rel": "self",
        }
    ],
    "totalItems": 5,
    "totalPages": 1,
}

MOCK_STATES = {
    "items": [
        "AK",
    ],
    "links": [
        {
            "href": "https://sandbox-api.va.gov/services/benefits-reference-data/v1/states",
            "rel": "self",
        }
    ],
    "totalItems": 1,
    "totalPages": 1,
}

MOCK_SPECIAL_CIRCUMSTANCES = {
    "items": [
        {"code": "AA", "description": "Automobile Allowance"},
        {"code": "IU", "description": "Individual Unemployability"},
        {"code": "SAH", "description": "Specially Adapted Housing"},
        {"code": "SAA", "description": "Spouse Aid and Attendance"},
        {"code": "SMC", "description": "Special Monthly Compensation"},
        {"code": "TTD", "description": "Temporary Total Disability"},
    ],
    "links": [
        {
            "href": "https://sandbox-api.va.gov/services/benefits-reference-data/v1/special-circumstances",
            "rel": "self",
        }
    ],
    "totalItems": 6,
    "totalPages": 1,
}

MOCK_MILITARY_PAY_TYPES = {
    "items": [
        {"code": "RTRMT", "description": "Longevity"},
        {"code": "TDRL", "description": "Temporary Disability Retired List (TDRL)"},
        {"code": "PDRL", "description": "Permanent Disability Retired List (PDRL)"},
        {"code": "SEP", "description": "Separation"},
        {"code": "SEV", "description": "Severance"},
    ],
    "links": [
        {
            "href": "https://sandbox-api.va.gov/services/benefits-reference-data/v1/military-pay-types",
            "rel": "self",
        }
    ],
    "totalItems": 5,
    "totalPages": 1,
}

MOCK_INTAKE_SITES = {
    "items": [
        {"description": "AF Academy", "id": 98283},
        {"description": "Al Udeid, Qatar", "id": 123657},
        {"description": "MCB Hawaii", "id": 98401},
    ],
    "links": [
        {
            "href": "https://sandbox-api.va.gov/services/benefits-reference-data/v1/intake-sites",
            "rel": "self",
        }
    ],
    "totalItems": 3,
    "totalPages": 1,
}

MOCK_DISABILITIES_DATA = {
    "items": [
        {
            "endDateTime": "2016-02-04T17:51:56Z",
            "id": 2650,
            "name": "foot condition, bilateral",
        },
    ],
    "links": [
        {
            "href": "https://sandbox-api.va.gov/services/benefits-reference-data/v1/disabilities",
            "rel": "self",
        }
    ],
    "totalItems": 1,
    "totalPages": 1,
}

MOCK_COUNTRIES = {
    "items": [
        "USA",
    ],
    "links": [
        {
            "href": "https://sandbox-api.va.gov/services/benefits-reference-data/v1/countries",
            "rel": "self",
        }
    ],
    "totalItems": 1,
    "totalPages": 1,
}
