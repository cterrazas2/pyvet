MOCK_LOCATION = {
    "link": [
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Location?_id=I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000&page=1&_count=30",
            "relation": "self",
        },
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Location?_id=I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000&page=1&_count=30",
            "relation": "first",
        },
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Location?_id=I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000&page=1&_count=30",
            "relation": "last",
        },
    ],
    "type": "searchset",
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Location/I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            "resource": {
                "id": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "mode": "instance",
                "name": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB",
                "type": [
                    {
                        "text": "OUTPATIENT CLINIC",
                        "coding": [{"display": "OUTPATIENT CLINIC"}],
                    }
                ],
                "status": "active",
                "address": {
                    "city": "LYONS",
                    "line": ["151 KNOLLCROFT ROAD"],
                    "text": "151 KNOLLCROFT ROAD LYONS NJ 07939",
                    "state": "NJ",
                    "postalCode": "07939",
                },
                "telecom": [{"value": "908-647-0180 EXT 4437", "system": "phone"}],
                "description": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
                "physicalType": {
                    "text": "BUILDING 7",
                    "coding": [{"display": "BUILDING 7"}],
                },
                "resourceType": "Location",
                "managingOrganization": {
                    "display": "LYONS VA MEDICAL CENTER",
                    "reference": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Organization/I2-TYIC2AW2NXNADER4SKRKJQZWRE000000",
                },
            },
        }
    ],
    "total": 1,
    "resourceType": "Bundle",
}

MOCK_LOCATION_ID = {
    "id": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
    "mode": "instance",
    "name": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB",
    "type": [
        {"text": "OUTPATIENT CLINIC", "coding": [{"display": "OUTPATIENT CLINIC"}]}
    ],
    "status": "active",
    "address": {
        "city": "LYONS",
        "line": ["151 KNOLLCROFT ROAD"],
        "text": "151 KNOLLCROFT ROAD LYONS NJ 07939",
        "state": "NJ",
        "postalCode": "07939",
    },
    "telecom": [{"value": "908-647-0180 EXT 4437", "system": "phone"}],
    "description": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
    "physicalType": {"text": "BUILDING 7", "coding": [{"display": "BUILDING 7"}]},
    "resourceType": "Location",
    "managingOrganization": {
        "display": "LYONS VA MEDICAL CENTER",
        "reference": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Organization/I2-TYIC2AW2NXNADER4SKRKJQZWRE000000",
    },
}

MOCK_ORG = {
    "link": [
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Organization?_id=I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000&_count=30&page=1",
            "relation": "first",
        },
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Organization?_id=I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000&_count=30&page=1",
            "relation": "self",
        },
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Organization?_id=I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000&_count=30&page=1",
            "relation": "last",
        },
    ],
    "type": "searchset",
    "entry": [
        {
            "search": {"mode": "match"},
            "fullUrl": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Organization/I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000",
            "resource": {
                "id": "I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000",
                "name": "CHEYENNE VA MEDICAL",
                "active": True,
                "address": [
                    {
                        "city": "CHEYENNE",
                        "line": ["2360 E PERSHING BLVD"],
                        "text": "2360 E PERSHING BLVD CHEYENNE WY 82001-5356",
                        "state": "WY",
                        "postalCode": "82001-5356",
                    }
                ],
                "identifier": [
                    {"value": "1164471991", "system": "http://hl7.org/fhir/sid/us-npi"},
                    {
                        "use": "usual",
                        "type": {
                            "text": "Facility ID",
                            "coding": [
                                {
                                    "code": "FI",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "display": "Facility ID",
                                }
                            ],
                        },
                        "value": "vha_442",
                        "system": "https://api.va.gov/services/provider-directory/v0/r4/NamingSystem/va-facility-identifier",
                    },
                ],
                "resourceType": "Organization",
            },
        }
    ],
    "total": 1,
    "resourceType": "Bundle",
}

MOCK_ORG_ID = {
    "id": "I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000",
    "name": "CHEYENNE VA MEDICAL",
    "active": True,
    "address": [
        {
            "city": "CHEYENNE",
            "line": ["2360 E PERSHING BLVD"],
            "text": "2360 E PERSHING BLVD CHEYENNE WY 82001-5356",
            "state": "WY",
            "postalCode": "82001-5356",
        }
    ],
    "identifier": [
        {"value": "1164471991", "system": "http://hl7.org/fhir/sid/us-npi"},
        {
            "use": "usual",
            "type": {
                "text": "Facility ID",
                "coding": [
                    {
                        "code": "FI",
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "display": "Facility ID",
                    }
                ],
            },
            "value": "vha_442",
            "system": "https://api.va.gov/services/provider-directory/v0/r4/NamingSystem/va-facility-identifier",
        },
    ],
    "resourceType": "Organization",
}

MOCK_PRACTITIONER = {
    "link": [
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Practitioner?_id=I2-HRJI2MVST2IQSPR7U5SACWIWZA000000&_count=30&page=1",
            "relation": "first",
        },
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Practitioner?_id=I2-HRJI2MVST2IQSPR7U5SACWIWZA000000&_count=30&page=1",
            "relation": "self",
        },
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Practitioner?_id=I2-HRJI2MVST2IQSPR7U5SACWIWZA000000&_count=30&page=1",
            "relation": "last",
        },
    ],
    "type": "searchset",
    "entry": [
        {
            "search": {"mode": "match"},
            "fullUrl": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
            "resource": {
                "id": "I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
                "name": [
                    {
                        "given": ["JANE460"],
                        "family": "DOE922",
                        "prefix": ["DR."],
                        "suffix": ["MD"],
                    }
                ],
                "active": True,
                "gender": "female",
                "address": [
                    {
                        "city": "CHEYENNE",
                        "line": ["555 E 5TH ST", "SUITE B"],
                        "state": "WYOMING",
                        "period": {"end": "2015-04-02", "start": "2010-01-01"},
                        "postalCode": "82001",
                    }
                ],
                "telecom": [
                    {"use": "work", "value": "555-555-1137", "system": "phone"},
                    {"use": "home", "value": "555-4055", "system": "phone"},
                    {"use": "mobile", "value": "5-541", "system": "pager"},
                ],
                "birthDate": "1964-02-23",
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {"code": "MR", "system": "http://hl7.org/fhir/v2/0203"}
                            ]
                        },
                        "value": "1015517260V990420",
                        "system": "http://va.gov/mpi",
                        "assigner": {"display": "Master Patient Index"},
                    },
                    {"value": "1932127842", "system": "http://hl7.org/fhir/sid/us-npi"},
                ],
                "resourceType": "Practitioner",
                "qualification": [{"code": {"text": "MD"}}],
            },
        }
    ],
    "total": 1,
    "resourceType": "Bundle",
}

MOCK_PRACTITIONER_ID = {
    "id": "I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
    "name": [
        {"given": ["JANE460"], "family": "DOE922", "prefix": ["DR."], "suffix": ["MD"]}
    ],
    "active": True,
    "gender": "female",
    "address": [
        {
            "city": "CHEYENNE",
            "line": ["555 E 5TH ST", "SUITE B"],
            "state": "WYOMING",
            "period": {"end": "2015-04-02", "start": "2010-01-01"},
            "postalCode": "82001",
        }
    ],
    "telecom": [
        {"use": "work", "value": "555-555-1137", "system": "phone"},
        {"use": "home", "value": "555-4055", "system": "phone"},
        {"use": "mobile", "value": "5-541", "system": "pager"},
    ],
    "birthDate": "1964-02-23",
    "identifier": [
        {
            "use": "usual",
            "type": {
                "coding": [{"code": "MR", "system": "http://hl7.org/fhir/v2/0203"}]
            },
            "value": "1015517260V990420",
            "system": "http://va.gov/mpi",
            "assigner": {"display": "Master Patient Index"},
        },
        {"value": "1932127842", "system": "http://hl7.org/fhir/sid/us-npi"},
    ],
    "resourceType": "Practitioner",
    "qualification": [{"code": {"text": "MD"}}],
}

MOCK_PRACTITIONER_ROLE = {
    "link": [
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/PractitionerRole?_id=I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000&_count=30&page=1",
            "relation": "first",
        },
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/PractitionerRole?_id=I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000&_count=30&page=1",
            "relation": "self",
        },
        {
            "url": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/PractitionerRole?_id=I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000&_count=30&page=1",
            "relation": "last",
        },
    ],
    "type": "searchset",
    "entry": [
        {
            "search": {"mode": "match"},
            "fullUrl": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/PractitionerRole/I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000",
            "resource": {
                "id": "I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000",
                "code": [
                    {
                        "text": "PSYCHOLOGIST",
                        "coding": [
                            {
                                "code": "PHYSICIAN",
                                "system": "http://hl7.org/fhir/practitioner-role",
                                "display": "PSYCHOLOGIST",
                            }
                        ],
                    }
                ],
                "active": True,
                "telecom": [
                    {"value": "555-555-1137", "system": "phone"},
                    {"value": "555-4055", "system": "phone"},
                    {"value": "5-541", "system": "pager"},
                ],
                "location": [
                    {
                        "display": "ZZCHY LASTNAME MEDICAL",
                        "reference": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Location/I2-3JYDMXC6RXTU4H25KRVXATSEJQ000000",
                    }
                ],
                "specialty": [
                    {
                        "coding": [
                            {
                                "code": "V111500",
                                "system": "http://nucc.org/provider-taxonomy",
                            }
                        ]
                    },
                    {
                        "coding": [
                            {
                                "code": "V111000",
                                "system": "http://nucc.org/provider-taxonomy",
                            }
                        ]
                    },
                    {
                        "coding": [
                            {
                                "code": "V110900",
                                "system": "http://nucc.org/provider-taxonomy",
                            }
                        ]
                    },
                    {
                        "coding": [
                            {
                                "code": "207Q00000X",
                                "system": "http://nucc.org/provider-taxonomy",
                            }
                        ]
                    },
                ],
                "organization": {
                    "display": "CHEYENNE VA MEDICAL",
                    "reference": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Organization/I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000",
                },
                "practitioner": {
                    "display": "DOE922,JANE460",
                    "reference": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
                },
                "resourceType": "PractitionerRole",
                "healthcareService": [{"display": "MEDICAL SERVICE"}],
            },
        }
    ],
    "total": 1,
    "resourceType": "Bundle",
}

MOCK_PRACTITIONER_ROLE_ID = {
    "id": "I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000",
    "code": [
        {
            "text": "PSYCHOLOGIST",
            "coding": [
                {
                    "code": "PHYSICIAN",
                    "system": "http://hl7.org/fhir/practitioner-role",
                    "display": "PSYCHOLOGIST",
                }
            ],
        }
    ],
    "active": True,
    "telecom": [
        {"value": "555-555-1137", "system": "phone"},
        {"value": "555-4055", "system": "phone"},
        {"value": "5-541", "system": "pager"},
    ],
    "location": [
        {
            "display": "ZZCHY LASTNAME MEDICAL",
            "reference": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Location/I2-3JYDMXC6RXTU4H25KRVXATSEJQ000000",
        }
    ],
    "specialty": [
        {
            "coding": [
                {"code": "V111500", "system": "http://nucc.org/provider-taxonomy"}
            ]
        },
        {
            "coding": [
                {"code": "V111000", "system": "http://nucc.org/provider-taxonomy"}
            ]
        },
        {
            "coding": [
                {"code": "V110900", "system": "http://nucc.org/provider-taxonomy"}
            ]
        },
        {
            "coding": [
                {"code": "207Q00000X", "system": "http://nucc.org/provider-taxonomy"}
            ]
        },
    ],
    "organization": {
        "display": "CHEYENNE VA MEDICAL",
        "reference": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Organization/I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000",
    },
    "practitioner": {
        "display": "DOE922,JANE460",
        "reference": "https://sandbox-api.va.gov/services/provider-directory/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
    },
    "resourceType": "PractitionerRole",
    "healthcareService": [{"display": "MEDICAL SERVICE"}],
}
