from abc import ABC, abstractclassmethod
from typing import NoReturn
import mlops_pipeline.utilities as utils


class DataDownloader(ABC):
    """
    Abstract class for downloading data from external sources.
    """

    @abstractclassmethod
    def download_data(self) -> NoReturn:
        """
        Abstract method for downloading data from external sources.
        """
        pass


class KaggleDataDownloader(DataDownloader):
    def download(self) -> NoReturn:
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
