# PyVet Architecture

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
    client.py                     # Where a session is created for a user
                                   (for applications that require persistence)
    creds.py                      # Where to store all credentials

/tests                            # All unit tests are here
    /benefits                     # Test the VA Benefits APIs
        test_benefits_intake.py   # Test the VA Benefits Intake API
    /data                         # Some mock data for testing
    .
    .
    .
```
