"""This module contains type aliases for json data."""
import requests

Json = (
    dict[str, "Json"]
    | list["Json"]
    | requests.Response
    | str
    | int
    | float
    | bool
    | None
)
