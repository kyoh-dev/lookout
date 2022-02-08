class DataQualityError(Exception):
    """Raise when an issue with a dataset's quality is detected"""


class DataTypeError(Exception):
    """Raise when an unexpected data type is read"""
