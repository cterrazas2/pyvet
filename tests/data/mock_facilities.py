MOCK_FACILITY = {
    "data": {
        "id": "vha_688",
        "type": "va_facilities",
        "attributes": {
            "name": "Washington VA Medical Center",
            "facility_type": "va_health_facility",
            "classification": "VA Medical Center (VAMC)",
            "website": "http://www.washingtondc.va.gov",
            "lat": 38.9311137,
            "long": -77.0109110499999,
            "time_zone": "America/New_York",
            "address": {
                "mailing": {
                    "zip": "20422-0001",
                    "city": "Washington",
                    "state": "DC",
                    "address_1": "50 Irving Street, Northwest",
                    "address_2": "Bldg 2",
                    "address_3": "Suite 7",
                },
                "physical": {
                    "zip": "20422-0001",
                    "city": "Washington",
                    "state": "DC",
                    "address_1": "50 Irving Street, Northwest",
                    "address_2": "Bldg 2",
                    "address_3": "Suite 7",
                },
            },
            "phone": "1-800-827-1000",
            "hours": '"monday": "9:30AM-4:00PM",',
            "operational_hours_special_instructions": "Normal business hours are Monday through Friday, 8:00 a.m. to 4:30 p.m.",
            "services": {
                "other": ["OnlineScheduling"],
                "health": ["Audiology"],
                "benefits": ["ApplyingForBenefits"],
                "last_updated": "2018-01-01",
            },
            "satisfaction": {
                "health": {
                    "primary_care_urgent": 0.85,
                    "primary_care_routine": 0.85,
                    "specialty_care_urgent": 0.85,
                    "specialty_care_routine": 0.85,
                },
                "effective_date": "2018-01-01",
            },
            "wait_times": 10,
            "mobile": False,
            "active_status": "A",
            "operating_status": "NORMAL",
            "detailed_services": [
                {
                    "service_id": "covid19Vaccine",
                    "name": "COVID-19 vaccines",
                    "description_facility": "null",
                    "appointment_leadin": "Your VA health care team will contact you if you???re eligible to get a vaccine during this time. As the supply of vaccine increases, we'll work with our care teams to let Veterans know their options.",
                    "appointment_phones": [
                        {
                            "extension": "71234",
                            "label": "Main phone",
                            "number": "937-268-6511",
                            "type": "tel",
                        }
                    ],
                    "online_scheduling_available": "True",
                    "referral_required": "False",
                    "walk_ins_accepted": "True",
                    "service_locations": [
                        {
                            "service_location_address": {
                                "building_name_number": "Baxter Building",
                                "clinic_name": "Baxter Clinic",
                                "wing_floor_or_room_number": "Wing East",
                                "address_line1": "50 Irving Street, Northwest",
                                "address_line2": "Bldg 2",
                                "city": "Washington",
                                "state": "DC",
                                "zip_code": "20422-0001",
                                "country_code": "US",
                            },
                            "appointment_phones": [
                                {
                                    "extension": "71234",
                                    "label": "Main phone",
                                    "number": "937-268-6511",
                                    "type": "tel",
                                }
                            ],
                            "email_contacts": [
                                {
                                    "email_address": "georgea@va.gov",
                                    "email_label": "George Anderson",
                                }
                            ],
                            "facility_service_hours": {
                                "Monday": "9AM-5PM",
                                "Tuesday": "9AM-5PM",
                                "Wednesday": "9AM-5PM",
                                "Thursday": "9AM-5PM",
                                "Friday": "9AM-5PM",
                                "Saturday": "Closed",
                                "Sunday": "Closed",
                            },
                            "additional_hours_info": "Location hours times may vary depending on staff availability",
                        }
                    ],
                    "path": "https://www.boston.va.gov/services/covid-19-vaccines.asp",
                }
            ],
            "visn": "20",
        },
    }
}

MOCK_FACILITIES = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [-77.0367761, 38.9004181]},
            "properties": {
                "id": "vha_688",
                "name": "Washington VA Medical Center",
                "facility_type": "va_health_facility",
                "classification": "VA Medical Center (VAMC)",
                "website": "http://www.washingtondc.va.gov",
                "time_zone": "America/New_York",
                "address": {
                    "mailing": {
                        "zip": "20422-0001",
                        "city": "Washington",
                        "state": "DC",
                        "address_1": "50 Irving Street, Northwest",
                        "address_2": "Bldg 2",
                        "address_3": "Suite 7",
                    },
                    "physical": {
                        "zip": "20422-0001",
                        "city": "Washington",
                        "state": "DC",
                        "address_1": "50 Irving Street, Northwest",
                        "address_2": "Bldg 2",
                        "address_3": "Suite 7",
                    },
                },
                "phone": "1-800-827-1000",
                "hours": '"monday": "9:30AM-4:00PM",',
                "operational_hours_special_instructions": '["More hours are available for some services.","If you need to talk to someone, call the Vet Center at 1-877-927-8387.","Vet Center hours are dependent upon outreach assignments."]',
                "services": {
                    "other": ["OnlineScheduling"],
                    "health": ["Audiology"],
                    "benefits": ["ApplyingForBenefits"],
                    "last_updated": "2018-01-01",
                },
                "satisfaction": {
                    "health": {
                        "primary_care_urgent": 0.85,
                        "primary_care_routine": 0.85,
                        "specialty_care_urgent": 0.85,
                        "specialty_care_routine": 0.85,
                    },
                    "effective_date": "2018-01-01",
                },
                "wait_times": 10,
                "mobile": False,
                "active_status": "A",
                "operating_status": "NORMAL",
                "visn": "20",
                "detailed_services": [
                    {
                        "service_id": "covid19Vaccine",
                        "name": "COVID-19 vaccines",
                        "description_facility": "null",
                        "appointment_leadin": "Your VA health care team will contact you if you???re eligible to get a vaccine during this time. As the supply of vaccine increases, we'll work with our care teams to let Veterans know their options.",
                        "appointment_phones": [
                            {
                                "extension": "71234",
                                "label": "Main phone",
                                "number": "937-268-6511",
                                "type": "tel",
                            }
                        ],
                        "online_scheduling_available": "True",
                        "referral_required": "False",
                        "walk_ins_accepted": "True",
                        "service_locations": [
                            {
                                "service_location_address": {
                                    "building_name_number": "Baxter Building",
                                    "clinic_name": "Baxter Clinic",
                                    "wing_floor_or_room_number": "Wing East",
                                    "address_line1": "50 Irving Street, Northwest",
                                    "address_line2": "Bldg 2",
                                    "city": "Washington",
                                    "state": "DC",
                                    "zip_code": "20422-0001",
                                    "country_code": "US",
                                },
                                "appointment_phones": [
                                    {
                                        "extension": "71234",
                                        "label": "Main phone",
                                        "number": "937-268-6511",
                                        "type": "tel",
                                    }
                                ],
                                "email_contacts": [
                                    {
                                        "email_address": "georgea@va.gov",
                                        "email_label": "George Anderson",
                                    }
                                ],
                                "facility_service_hours": {
                                    "Monday": "9AM-5PM",
                                    "Tuesday": "9AM-5PM",
                                    "Wednesday": "9AM-5PM",
                                    "Thursday": "9AM-5PM",
                                    "Friday": "9AM-5PM",
                                    "Saturday": "Closed",
                                    "Sunday": "Closed",
                                },
                                "additional_hours_info": "Location hours times may vary depending on staff availability",
                            }
                        ],
                        "path": "https://www.boston.va.gov/services/covid-19-vaccines.asp",
                    }
                ],
            },
        }
    ],
}

MOCK_FACILITY_IDS = {
    "data": [
        "vc_0101V",
        "vc_0102V",
        "vc_0103V",
        "vc_0104V",
        "vc_0105V",
        "vc_0106V",
        "vc_0107V",
        "vc_0108V",
        "vc_0109V",
        "vc_0110V",
        "nca_042",
        "nca_054",
        "nca_055",
        "nca_058",
        "nca_059",
        "nca_075",
        "nca_076",
        "nca_077",
        "nca_078",
        "nca_079",
        "nca_080",
        "nca_081",
        "vc_0810MVC",
        "vc_0811MVC",
        "vc_0812MVC",
        "vc_0813MVC",
        "vc_0814MVC",
        "vc_0815MVC",
        "vc_0816MVC",
        "vc_0817MVC",
        "vc_0818MVC",
        "vc_0819MVC",
        "vc_0820MVC",
        "vc_0821MVC",
        "vc_0822MVC",
        "vc_0823MVC",
        "vc_0824MVC",
        "vc_0825MVC",
        "vc_0826MVC",
        "vc_0827MVC",
        "vc_0828MVC",
        "vc_0829MVC",
        "vc_0830MVC",
        "vc_0831MVC",
        "vc_0832MVC",
        "vc_0833MVC",
        "vc_0857MVC",
        "vc_0858MVC",
        "vc_0859MVC",
        "vc_0860MVC",
        "vc_0861MVC",
        "vc_0862MVC",
        "vc_0863MVC",
        "vc_0864MVC",
        "vc_0865MVC",
        "vc_0866MVC",
        "vc_0867MVC",
        "vc_0868MVC",
        "vc_0869MVC",
        "vc_0870MVC",
        "vc_0871MVC",
        "vc_0872MVC",
        "vc_0873MVC",
        "vc_0874MVC",
        "vc_0875MVC",
        "vc_0876MVC",
        "vc_0877MVC",
        "vc_0879MVC",
        "vc_0880MVC",
        "vc_0881MVC",
        "vc_0882MVC",
        "vc_0883MVC",
        "vc_0885MVC",
        "vc_0886MVC",
        "nca_089",
        "vc_1081OS",
        "nca_120",
        "nca_121",
        "nca_122",
        "vc_1221OS",
        "nca_123",
        "vc_2081OS",
        "vc_2091OS",
        "vc_2092OS",
        "vba_301",
        "vba_301a",
        "vba_301b",
        "vba_304",
        "vba_304a",
        "vba_304h",
        "vba_304j",
        "vba_304k",
        "vba_306",
        "vba_306a",
        "vba_306b",
        "vba_306d",
        "vba_306f",
        "vba_306g",
        "vba_306h",
        "vba_306i",
        "vba_306j",
        "vba_307",
        "vc_3071OS",
        "vc_3072OS",
        "vba_307a",
        "vba_307b",
        "vba_307c",
        "vba_307d",
        "vba_307e",
        "vba_307f",
        "vba_308",
        "vba_308b",
        "vba_308d",
        "vba_309",
        "vba_310",
        "vba_310a",
        "vba_310b",
        "vba_310e",
        "vba_310g",
        "vba_310h",
        "vba_311",
        "vba_311a",
        "vba_311b",
        "vba_313",
        "vba_313a",
        "vba_313b",
        "vba_313c",
        "vba_313d",
        "vba_313e",
        "vba_313f",
        "vba_314",
        "vba_314aa",
        "vba_314ab",
        "vba_314b",
        "vba_314c",
        "vba_314e",
        "vba_314g",
        "vba_314h",
        "vba_314i",
        "vba_314j",
        "vba_314k",
        "vba_314l",
        "vba_314m",
        "vba_314n",
        "vba_314o",
        "vba_314q",
        "vba_314v",
        "vba_315",
        "vba_315d",
        "vba_315e",
        "vba_315f",
        "vba_315g",
        "vba_315h",
        "vba_316",
        "vba_316a",
        "vba_316b",
        "vba_316c",
        "vba_316d",
        "vba_316e",
        "vba_316f",
        "vba_316g",
        "vba_316h",
        "vba_316i",
        "vba_316j",
        "vba_316k",
        "vba_316n",
        "vba_316o",
        "vba_316p",
        "vba_317",
        "vba_317a",
        "vba_317aa",
        "vba_317ab",
        "vba_317ac",
        "vba_317ad",
        "vba_317ae",
        "vba_317af",
        "vba_317ai",
        "vba_317b",
        "vba_317c",
        "vba_317d",
        "vba_317e",
        "vba_317f",
        "vba_317g",
        "vba_317h",
        "vba_317i",
        "vba_317j",
        "vba_317k",
        "vba_317l",
        "vba_317m",
        "vba_317o",
        "vba_317p",
        "vba_317q",
        "vba_317r",
        "vba_317s",
        "vba_317t",
        "vba_317u",
        "vba_317v",
        "vba_317w",
        "vba_317x",
        "vba_317y",
        "vba_317z",
        "vba_318",
        "vba_318a",
        "vba_318c",
        "vba_318d",
        "vba_318e",
        "vba_318f",
        "vba_318h",
        "vba_318l",
        "vba_318m",
        "vba_318p",
        "vba_318q",
        "vba_318r",
        "vba_319",
        "vba_319a",
        "vba_319b",
        "vba_319c",
        "vba_319d",
        "vba_319e",
        "vba_319f",
        "vba_319g",
        "vba_319h",
        "vba_319i",
        "vba_320",
        "vba_320a",
        "vba_320b",
        "vba_320c",
        "vba_320d",
        "vba_320f",
        "vba_320g",
        "vba_321",
        "vba_321a",
        "vba_321b",
        "vba_321e",
        "vba_322",
        "vba_322c",
        "vba_322d",
        "vba_322e",
        "vba_322f",
        "vba_322g",
        "vba_322h",
        "vba_322i",
        "vba_322j",
        "vba_322k",
        "vba_322l",
        "vba_322m",
        "vba_322n",
        "vba_322o",
        "vba_322p",
        "vba_323",
        "vba_323a",
        "vba_323b",
        "vba_323c",
        "vba_323d",
        "vba_325",
        "vba_325a",
        "vba_325b",
        "vba_325c",
        "vba_325d",
        "vba_329h",
        "vba_329i",
        "vba_329j",
        "vba_329k",
        "vba_329l",
        "vba_329m",
        "vba_329n",
        "vba_329o",
        "vba_329p",
        "vba_330",
        "vba_330a",
        "vba_330b",
        "vba_330c",
        "vba_330f",
        "vba_331",
        "vba_331a",
        "vba_331b",
        "vba_331d",
        "vba_331e",
        "vba_331f",
        "vba_331h",
        "vba_333",
        "vba_333a",
        "vba_333b",
        "vba_333c",
        "vba_333d",
        "vba_333e",
        "vba_334",
        "vba_334a",
        "vba_334b",
        "vba_334c",
        "vba_334d",
        "vba_334e",
        "vba_334f",
        "vba_334g",
        "vba_334i",
        "vba_335",
        "vba_335a",
        "vba_335b",
        "vba_335c",
        "vba_335d",
        "vba_339",
        "vba_339a",
        "vba_339b",
        "vba_339c",
        "vba_339d",
        "vba_340",
        "vba_340a",
        "vba_340b",
        "vba_341",
        "vba_341a",
        "vba_341b",
        "vba_341c",
        "vba_341d",
        "vba_341e",
        "vba_341f",
        "vba_341g",
        "vba_343",
        "vba_343a",
        "vba_343ao",
        "vba_343ar",
        "vba_343as",
        "vba_343at",
        "vba_343b",
        "vba_343c",
        "vba_343d",
        "vba_343e",
        "vba_343g",
        "vba_343q",
        "vba_344",
        "vba_344a",
        "vba_344b",
        "vba_344c",
        "vba_344d",
        "vba_344e",
        "vba_344f",
        "vba_344g",
        "vba_344h",
        "vba_344i",
        "vba_344j",
        "vba_344k",
        "vba_348b",
        "vba_348d",
        "vba_348h",
        "vba_349",
        "vba_349a",
        "vba_349ab",
        "vba_349ac",
        "vba_349b",
        "vba_349c",
        "vba_349d",
        "vba_349e",
        "vba_349f",
        "vba_349g",
        "vba_349h",
        "vba_349i",
        "vba_349k",
        "vba_349m",
        "vba_349n",
        "vba_349o",
        "vba_349p",
        "vba_349q",
        "vba_349s",
        "vba_349t",
        "vba_349u",
        "vba_349v",
        "vba_349w",
        "vba_349x",
        "vba_349z",
        "vba_350",
        "vba_350a",
        "vba_350b",
        "vba_350c",
        "vba_350d",
        "vba_350e",
        "vba_350f",
        "vba_350g",
        "vba_351",
        "vba_351a",
        "vba_351b",
        "vba_351c",
        "vba_351d",
        "vba_351e",
        "vba_351f",
        "vba_351g",
        "vba_351i",
        "vba_354",
        "vba_354a",
        "vba_354b",
        "vba_354c",
        "vba_355",
        "vba_355b",
        "vba_355c",
        "vba_355d",
        "vba_355e",
        "vba_355f",
        "vba_355h",
        "vba_355i",
        "vba_358",
        "vha_358",
        "vba_362",
        "vba_362a",
        "vba_362d",
        "vba_362e",
        "vba_377d",
        "vba_377e",
        "vba_377f",
        "vba_377g",
        "vba_377h",
        "vba_377i",
        "vba_377j",
        "vba_377k",
        "vba_377l",
        "vba_377m",
        "vba_377n",
        "vba_402",
        "vha_402",
        "vha_402GA",
        "vha_402GB",
        "vha_402GC",
        "vha_402GE",
        "vha_402GF",
        "vha_402HB",
        "vha_402HC",
        "vha_402HL",
        "vha_402QA",
        "vha_402QB",
        "vba_405",
        "vha_405",
        "vha_405GA",
        "vha_405GC",
        "vha_405HA",
        "vha_405HC",
        "vha_405HE",
        "vha_405HF",
        "vha_405QB",
        "vc_4061OS",
        "vba_436",
        "vha_436",
        "vha_436A4",
        "vba_436b",
        "vba_437",
        "vha_437",
        "vba_437a",
        "vha_437GA",
        "vha_437GB",
        "vha_437GC",
        "vha_437GD",
        "vha_437GE",
        "vha_437GF",
        "vha_437GI",
        "vha_437GJ",
        "vha_437GK",
        "vha_437GL",
        "vha_437QA",
        "vba_438",
        "vha_438",
        "vba_438a",
        "vba_438b",
        "vba_438c",
        "vha_438GA",
        "vha_438GC",
        "vha_438GD",
        "vha_438GE",
        "vha_438GF",
        "vba_442",
        "vha_442",
        "vba_452",
        "vba_452a",
        "vba_452b",
        "vba_452c",
        "vba_452d",
        "nca_800",
        "nca_801",
        "nca_802",
        "nca_803",
        "nca_804",
        "nca_805",
        "nca_806",
        "nca_807",
        "nca_808",
        "nca_809",
        "nca_810",
        "nca_811",
        "nca_812",
        "nca_813",
        "nca_814",
        "nca_900",
        "nca_s1001",
        "nca_s1002",
        "nca_s1003",
    ]
}
MOCK_NEARBY = {
    "data": {
        "id": "vha_600QA",
        "type": "va_facilities",
        "attributes": {
            "name": "West Santa Ana VA Clinic",
            "facility_type": "va_health_facility",
            "classification": "Other Outpatient Services (OOS)",
            "website": "https://www.va.gov/long-beach-health-care/locations/west-santa-ana-va-clinic/",
            "lat": 33.747642,
            "long": -117.8760285,
            "time_zone": "America/Los_Angeles",
            "address": {
                "mailing": {},
                "physical": {
                    "zip": "92701-4561",
                    "city": "Santa Ana",
                    "state": "CA",
                    "address_1": "888 West Santa Ana Boulevard",
                    "address_2": "Community Resource & Referral Center (CRRC)",
                    "address_3": "Suite 150",
                },
            },
            "phone": {
                "fax": "562-346-3542",
                "main": "844-838-8300",
                "pharmacy": "562-826-5744",
                "after_hours": "877-424-3838",
                "patient_advocate": "562-826-8000 x5467",
                "enrollment_coordinator": "562-826-8000 x5915",
                "health_connect": None,
            },
            "hours": {
                "monday": "800AM-400PM",
                "tuesday": "800AM-400PM",
                "wednesday": "800AM-400PM",
                "thursday": "800AM-400PM",
                "friday": "800AM-400PM",
                "saturday": "Closed",
                "sunday": "Closed",
            },
            "operational_hours_special_instructions": None,
            "services": {"other": [], "health": [], "last_updated": None},
            "satisfaction": {"health": {}, "effective_date": None},
            "wait_times": {"health": [], "effective_date": None},
            "mobile": False,
            "active_status": "A",
            "operating_status": {"code": "NORMAL"},
            "detailed_services": None,
            "visn": "22",
        },
    }
}

MOCK_QUERY_JSON = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [-77.0367761, 38.9004181]},
            "properties": {
                "id": "vha_688",
                "name": "Washington VA Medical Center",
                "facility_type": "va_health_facility",
                "classification": "VA Medical Center (VAMC)",
                "website": "http://www.washingtondc.va.gov",
                "time_zone": "America/New_York",
                "address": {
                    "mailing": {
                        "zip": "20422-0001",
                        "city": "Washington",
                        "state": "DC",
                        "address_1": "50 Irving Street, Northwest",
                        "address_2": "Bldg 2",
                        "address_3": "Suite 7",
                    },
                    "physical": {
                        "zip": "20422-0001",
                        "city": "Washington",
                        "state": "DC",
                        "address_1": "50 Irving Street, Northwest",
                        "address_2": "Bldg 2",
                        "address_3": "Suite 7",
                    },
                },
                "phone": "1-800-827-1000",
                "hours": '"monday": "9:30AM-4:00PM",',
                "operational_hours_special_instructions": '["More hours are available for some services.","If you need to talk to someone, call the Vet Center at 1-877-927-8387.","Vet Center hours are dependent upon outreach assignments."]',
                "services": {
                    "other": ["OnlineScheduling"],
                    "health": ["Audiology"],
                    "benefits": ["ApplyingForBenefits"],
                    "last_updated": "2018-01-01",
                },
                "satisfaction": {
                    "health": {
                        "primary_care_urgent": 0.85,
                        "primary_care_routine": 0.85,
                        "specialty_care_urgent": 0.85,
                        "specialty_care_routine": 0.85,
                    },
                    "effective_date": "2018-01-01",
                },
                "wait_times": 10,
                "mobile": False,
                "active_status": "A",
                "operating_status": "NORMAL",
                "visn": "20",
                "detailed_services": [
                    {
                        "service_id": "covid19Vaccine",
                        "name": "COVID-19 vaccines",
                        "description_facility": "null",
                        "appointment_leadin": "Your VA health care team will contact you if you???re eligible to get a vaccine during this time. As the supply of vaccine increases, we'll work with our care teams to let Veterans know their options.",
                        "appointment_phones": [
                            {
                                "extension": "71234",
                                "label": "Main phone",
                                "number": "937-268-6511",
                                "type": "tel",
                            }
                        ],
                        "online_scheduling_available": "True",
                        "referral_required": "False",
                        "walk_ins_accepted": "True",
                        "service_locations": [
                            {
                                "service_location_address": {
                                    "building_name_number": "Baxter Building",
                                    "clinic_name": "Baxter Clinic",
                                    "wing_floor_or_room_number": "Wing East",
                                    "address_line1": "50 Irving Street, Northwest",
                                    "address_line2": "Bldg 2",
                                    "city": "Washington",
                                    "state": "DC",
                                    "zip_code": "20422-0001",
                                    "country_code": "US",
                                },
                                "appointment_phones": [
                                    {
                                        "extension": "71234",
                                        "label": "Main phone",
                                        "number": "937-268-6511",
                                        "type": "tel",
                                    }
                                ],
                                "email_contacts": [
                                    {
                                        "email_address": "georgea@va.gov",
                                        "email_label": "George Anderson",
                                    }
                                ],
                                "facility_service_hours": {
                                    "Monday": "9AM-5PM",
                                    "Tuesday": "9AM-5PM",
                                    "Wednesday": "9AM-5PM",
                                    "Thursday": "9AM-5PM",
                                    "Friday": "9AM-5PM",
                                    "Saturday": "Closed",
                                    "Sunday": "Closed",
                                },
                                "additional_hours_info": "Location hours times may vary depending on staff availability",
                            }
                        ],
                        "path": "https://www.boston.va.gov/services/covid-19-vaccines.asp",
                    }
                ],
            },
        }
    ],
}
