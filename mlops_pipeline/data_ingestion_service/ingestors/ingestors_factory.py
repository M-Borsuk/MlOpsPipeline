import mlops_pipeline.data_ingestion_service.ingestor_utilities.custom_exceptions as ingestion_exceptions
from DataDownloader import DataDownloader, KaggleDataDownloader
from DataIngestor import DataIngestor, CSVDataIngestor


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
            config = ingestion_exceptions.KaggleConfig(**configuration)
        except Exception as e:
            raise ingestion_exceptions.WrongConfigError(configuration, str(e))
        ingestor = KaggleDataDownloader(config)
        return ingestor
    else:
        raise ingestion_exceptions.UnknownIngestorError(downloader_type)


def build_ingestor(ingestor_type: str, configuration: dict) -> DataIngestor:
    """The builder function for the Ingestor given the ingestor type.

    Parameters:
    ingestor_type {str} -- The type to create the given Ingestor class.
    configuration {dict} -- The configuration for the Ingestor class.

    Returns:
    An instance of a DataIngestor.
    """
    if ingestor_type.lower() == "csv":
        try:
            config = ingestion_exceptions.KaggleConfig(**configuration)
        except Exception as e:
            raise ingestion_exceptions.WrongConfigError(configuration, str(e))
        ingestor = CSVDataIngestor(config)
        return ingestor
    else:
        raise ingestion_exceptions.UnknownIngestorError(ingestor_type)
