from sys import stdout
from logging import INFO, basicConfig, captureWarnings


def setup_logging() -> None:
    basicConfig(stream=stdout, level=INFO)
    captureWarnings(True)
