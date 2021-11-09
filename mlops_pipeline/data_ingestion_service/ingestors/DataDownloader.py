from abc import ABC, abstractclassmethod
from typing import NoReturn
import mlops_pipeline.utilities as utils


class DataIngestor(ABC):
    def __init__(self, config: utils.Config) -> NoReturn:
        self.config = config

    @abstractclassmethod
    def download(self) -> NoReturn:
        pass


class KaggleDataIngestor(DataIngestor):
    def download(self) -> NoReturn:
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
