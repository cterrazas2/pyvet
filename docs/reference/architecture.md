# PyVet Architecture

`pyvet` is a python library that helps organizations, companies, and even veterans themselves analyze and research data from the Department of Veterans Affairs. This document outlines the quickest way to start contributing and get familiar with the code base.

## Code Setup

```console
/pyvet                            # This is where the main code lives
    /benefits                     # The VA Benefits APIs
        /intake                   # The VA Benefit Intake API
            api.py                # All apis have this file
        /reference                # The VA Benefits Reference API
        ...
    /facilities                   # The VA <name> API
    .
    .
    .
    client.py                     # Where a session is created for a user (for applications that require persistence)
    creds.py                      # Where to store all credentials

/tests                            # All unit tests are here
    /benefits                     # Test the VA Benefits APIs
        test_benefits_intake.py   # Test the VA Benefits Intake API
    /data                         # Some mock data for testing
    .
    .
    .
```
