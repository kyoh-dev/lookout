class DataQualityError(Exception):
    """Raise when an issue with a dataset's quality is detected"""


class MetadataError(Exception):
    """Raise when an unexpected metadata value is read from an input file"""
