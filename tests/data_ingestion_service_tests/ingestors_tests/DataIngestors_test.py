import pytest
import mlops_pipeline.data_ingestion_service.ingestors.DataIngestor as ingestors
import mlops_pipeline.data_ingestion_service.ingestors.DataDownloader as downloaders
import mlops_pipeline.data_ingestion_service.ingestors.ingestors_factory as ingestors_factory
from typing import NoReturn, Callable
import pandas as pd


@pytest.mark.parametrize(
    "downloader_type,configuration",
    [
        (
            "KAGGLE",
            {
                "download_url": "https://www.kaggle.com/datasets/titanic",
                "output_path": "titanic.csv",
                "user_name": "test_user",
                "api_key": "175f1735gv",
            },
        )
    ],
)
def test_downloader_factory(downloader_type: str, configuration: dict) -> NoReturn:
    """
    Test downloader factory
    :param downloader_type: type of downloader
    :param configuration: configuration for downloader
    :return:
    """
    downloader = ingestors_factory.build_downloader(downloader_type, configuration)
    assert isinstance(downloader, downloaders.DataDownloader)


@pytest.mark.parametrize(
    "ingestor_type,reader_function,configuration",
    [
        (
            "LOcal",
            pd.read_csv,
            {"input_path": "titanic.csv"},
        ),
        (
            "s3",
            pd.read_sql,
            {
                "input_path": "titanic.csv",
                "s3_access_key": "175f1735gv",
                "s3_secret_key": "175f1735gv",
                "s3_region": "eu-west-4",
                "s3_endpoint_url": "https://s3.eu-west-4.amazonaws.com",
                "read_options": {"error_bad_lines": False},
            },
        ),
    ],
)
def test_ingest_factory(
    ingestor_type: str, reader_function: Callable, configuration: dict
) -> NoReturn:
    """
    Test ingestor factory
    :param ingestor_type: type of ingestor
    :param configuration: configuration for ingestor
    :return:
    """
    ingestor = ingestors_factory.build_ingestor(
        ingestor_type, reader_function, configuration
    )
    assert isinstance(ingestor, ingestors.DataIngestor)
