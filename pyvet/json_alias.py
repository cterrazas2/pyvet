# This is a custom json type for type hinting.
Json = dict[str, "Json"] | list["Json"] | str | int | float | bool | None
