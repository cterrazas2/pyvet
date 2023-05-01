# PyVet

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python library to research and analyze veteran data from the
[Veterans Affairs](https://github.com/department-of-veterans-affairs) (VA)
Lighthouse API.

The [VA Lighthouse API](https://developer.va.gov) provides different types of
veteran data through a subset of the following apis
(internal VA apis are not supported):

Open Data APIS

- Benefits API
- Facilities API
- Forms API
- Health API
- Veteran Confirmation API

Auth APIS (OIDC)

- Benefits API
- Health API
- Veteran Verification API

You can find more information about these APIS and request API access
[here](https://developer.va.gov/onboarding/request-sandbox-access).

## Key documentation

The documentation can be browsed in the [docs](docs) folder, and key documents
are linked below.

- [Installation](docs/how-to/installation.md)
- [Quick start](docs/tutorials/quick_start.md)
- [Open Data API example requests](docs/tutorials/open_data_apis.md)
- [Oauth API example requests](docs/tutorials/oauth2_apis.md)
- [Run Tests](docs/how-to/run_tests.md)
- [Architecture](docs/reference/architecture.md)
- [Code Style](docs/reference/style.md)
- [Authorization](docs/explanation/authorization.md)
