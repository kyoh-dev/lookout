import re
from typing import Optional


def clean_uppercase(value: str) -> Optional[str]:
    """Strip and capitalise a value, and set it to None if the string equals `None`"""
    value = re.sub(" +", " ", value).strip().capitalize()
    if value.upper() == "NONE":
        return None

    return value


def clean_descr(value: str) -> str:
    """Strip a value and add a full-stop at the end if there isn't one"""
    value = re.sub(" +", " ", value).strip()
    if not value.endswith("."):
        value += "."

    return value
