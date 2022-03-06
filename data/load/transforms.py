import re
from typing import Optional


def strip_and_capitalise(value: str) -> Optional[str]:
    """Strip and capitalise a value, and set it to None if the string equals `None`"""
    value = re.sub(" +", " ", value).strip().capitalize()
    if value.upper() == "NONE":
        return None

    return value


def strip_and_punctuate(value: str) -> str:
    """Strip a value and add a full-stop at the end if there isn't one"""
    value = re.sub(" +", " ", value).strip()
    if not value.endswith("."):
        value += "."

    return value
