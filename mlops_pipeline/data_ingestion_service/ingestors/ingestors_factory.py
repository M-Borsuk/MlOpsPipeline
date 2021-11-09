import mlops_pipeline.data_ingestion_service.ingestor_utilities.custom_exceptions as ingestion_exceptions
from DataDownloader import DataIngestor, KaggleDataIngestor


def build_ingestor(ingestor_type: str, configuration: dict) -> DataIngestor:
    """The builder function for the Ingestor given the ingestor type.

    Parameters:
    ingestor_type {str} -- The type to create the given Ingestor class.
    configuration {dict} -- The configuration for the Ingestor class.

    Returns:
    An instance of a DataIngestor.
    """
    if ingestor_type.lower() == "kaggle":
        try:
            config = ingestion_exceptions.KaggleConfig(**configuration)
        except Exception as e:
            raise ingestion_exceptions.WrongConfigError(configuration, str(e))
        ingestor = KaggleDataIngestor(config)
        return ingestor
    else:
        raise ingestion_exceptions.UnknownIngestorError(ingestor_type)
