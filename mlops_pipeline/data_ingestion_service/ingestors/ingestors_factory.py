from typing import Callable
import mlops_pipeline.data_ingestion_service.ingestor_utilities.custom_exceptions as ingestion_exceptions
import mlops_pipeline.data_ingestion_service.ingestor_utilities.custom_configs as ingestion_config
from .DataDownloader import DataDownloader, KaggleDataDownloader
from .DataIngestor import DataIngestor, S3DataIngestor, LocalFSDataIngestor


def build_downloader(downloader_type: str, configuration: dict) -> DataDownloader:
    """The builder function for the Downloader given the downloader type.

    Parameters:
    downloader_type {str} -- The type to create the given Downloader class.
    configuration {dict} -- The configuration for the Downloader class.

    Returns:
    An instance of a DataDownloader.
    """
    if downloader_type.lower() == "kaggle":
        try:
            config = ingestion_config.KaggleConfig(**configuration)
        except Exception as e:
            raise ingestion_exceptions.WrongConfigError(configuration, str(e))
        ingestor = KaggleDataDownloader(config)
        return ingestor
    else:
        raise ingestion_exceptions.UnknownIngestorError(downloader_type)


def build_ingestor(
    ingestor_type: str, reader_function: Callable, configuration: dict
) -> DataIngestor:
    """The builder function for the Ingestor given the ingestor type.

    Parameters:
    ingestor_type {str} -- The type to create the given Ingestor class.
    configuration {dict} -- The configuration for the Ingestor class.

    Returns:
    An instance of a DataIngestor.
    """
    if ingestor_type.lower() == "local":
        try:
            config = ingestion_config.LocalFSDataIngestorConfig(**configuration)
        except Exception as e:
            raise ingestion_exceptions.WrongConfigError(configuration, str(e))
        ingestor = LocalFSDataIngestor(config, reader_function)
        return ingestor
    elif ingestor_type.lower() == "s3":
        try:
            config = ingestion_config.S3DataIngestorConfig(**configuration)
        except Exception as e:
            raise ingestion_exceptions.WrongConfigError(configuration, str(e))
        ingestor = S3DataIngestor(config, reader_function)
        return ingestor
    else:
        raise ingestion_exceptions.UnknownIngestorError(ingestor_type)
