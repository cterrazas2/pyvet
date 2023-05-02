"""This module contains type aliases for json data.""" ""
Json = dict[str, "Json"] | list["Json"] | str | int | float | bool | None
