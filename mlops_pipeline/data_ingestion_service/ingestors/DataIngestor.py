from abc import ABC, abstractclassmethod
from typing import NoReturn
import mlops_pipeline.utilities as utils
import pandas as pd


class DataIngestor(ABC):
    """
    Abstract class for ingesting data into the pipeline.
    """

    def __init__(self, config: utils.Config) -> NoReturn:
        self.config = config

    @abstractclassmethod
    def read(self) -> pd.DataFrame:
        """
        Abstract method for reading data into the pipeline.
        """
        pass


class CSVDataIngestor(DataIngestor):
    """
    The data ingestor class designed to ingest the csv files into the pipeline.
    """

    def __init__(self, config: utils.Config) -> NoReturn:
        super().__init__(config)

    def read(self) -> pd.DataFrame:
        """
        Reads the csv files into the pipeline.
        """
        return pd.read_csv(self.config.data_path)
