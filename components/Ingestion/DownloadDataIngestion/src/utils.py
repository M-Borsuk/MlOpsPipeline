from dataclasses import dataclass
import DataDownloader as ingestors
from typing import NoReturn
import yaml


@dataclass
class Config:
    """Base configuration dataclass for DownloadDataIngestors."""

    download_url: str
    output_path: str


@dataclass
class KaggleConfig(Config):
    """Configuration dataclass for kaggle related datasets"""

    user_name: str
    api_key: str


class Error(Exception):
    """Base class for other exceptions"""

    pass


class KaggleDownloadError(Error):
    """Raised when the kaggle dataset is not downloaded"""

    def __init__(self, command: str, error_message: str) -> NoReturn:
        self.command = command
        self.error_message = error_message
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return "Command {0} did not work. The error message -> {1}".format(
            self.command, self.error_message
        )


class WrongConfigError(Error):
    """Raised when the Config dataclass is not created"""

    def __init__(self, configuration: dict, error_message: str) -> NoReturn:
        self.configuration = configuration
        self.error_message = error_message
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return "The configuration {0} did not work.\
                The error message -> {1}".format(
            self.configuration, self.error_message
        )


class UnknownIngestorError(Error):
    """Raised when the Ingestor type is not known"""

    def __init__(self, ingestor_type: str) -> NoReturn:
        self.ingestor_type = ingestor_type

    def __str__(self) -> str:
        return "Unknown ingestor type -> {0}".format(self.ingestor_type)


def load_yaml(yaml_file: str) -> dict:
    """Function to load the configuration from a YAML file into a python dictionary

    Parameters:
    yaml_file {str} -- The path for the YAML file.

    Returns:
    A dictionary containing the configuration information.
    """

    file_stream = open(yaml_file, "r")
    config = yaml.load(file_stream)
    return config


def build_ingestor(ingestor_type: str,
                   configuration: dict) -> ingestors.DataIngestor:
    """The builder function for the Ingestor given the ingestor type.

    Parameters:
    ingestor_type {str} -- The type to create the given Ingestor class.
    configuration {dict} -- The configuration for the Ingestor class.

    Returns:
    An instance of a DataIngestor.
    """
    if ingestor_type.lower() == "kaggle":
        try:
            config = KaggleConfig(**configuration)
        except Exception as e:
            raise WrongConfigError(configuration, str(e))
        ingestor = ingestors.KaggleIngestor(config)
        return ingestor
    else:
        raise UnknownIngestorError(ingestor_type)
