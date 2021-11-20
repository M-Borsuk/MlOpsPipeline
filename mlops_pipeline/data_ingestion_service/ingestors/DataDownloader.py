from abc import ABC, abstractclassmethod
from typing import NoReturn
import mlops_pipeline.data_ingestion_service.ingestor_utilities.custom_configs as utils


class DataDownloader(ABC):
    """
    Abstract class for downloading data from external sources.
    """
    def __init__(
        self, config: utils.DataIngestorConfig,
    ) -> NoReturn:
        self.config = config

    @abstractclassmethod
    def download_data(self) -> NoReturn:
        """
        Abstract method for downloading data from external sources.
        """
        pass


class KaggleDataDownloader(DataDownloader):
    def download_data(self) -> NoReturn:
        """
        Download data from Kaggle.
        """
        import os

        os.environ["KAGGLE_USERNAME"] = self.config.user_name
        os.environ["KAGGLE_KEY"] = self.config.api_key
        command = "kaggle datasets download -p {0} --unzip --quiet {1}".format(
            self.config.output_path, self.config.download_url
        )
        try:
            os.system(command)
        except Exception as e:
            raise utils.KaggleDownloadError(command, str(e))
