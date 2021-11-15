from abc import ABC, abstractclassmethod
from typing import List, NoReturn
import mlops_pipeline.utilities as utils
import pandas as pd
import mlops_pipeline.logger as logger
import os
import boto3


class DataIngestor(ABC):
    """
    Abstract class for ingesting data into the pipeline.
    """

    def __init__(
        self, config: utils.DataIngestorConfig, reader_function: pd.DataReaderFunction
    ) -> NoReturn:
        self.config = config
        self.reader_function = reader_function

    def read(self) -> pd.DataFrame:
        """
        Base method for reading data into the pipeline using the reader_function.
        """
        logger.logger.info(f"Reading data from {self.config.data_path}")
        return self.reader_function(self.config.data_path, **self.config.reader_options)

    def read_table_combination(self) -> List[pd.DataFrame]:
        """
        Base method for reading data from multiple different files into the pipeline using the reader_function.
        """
        logger.logger.info(f"Reading data from {self.config.data_path}")
        data_frames = []
        for file in self.list_files():
            data_frames.append(self.reader_function(file, **self.config.reader_options))
        return data_frames

    @abstractclassmethod
    def create_directory(self, path: str) -> NoReturn:
        """
        Abstract method for creating a directory.
        """
        pass

    @abstractclassmethod
    def list_files(self):
        """
        Abstract method for listing files in a directory.
        """
        pass


class LocalFSDataIngestor(DataIngestor):
    """
    The data ingestor class designed to ingest the files into the pipeline from the local file storage.
    """

    def __init__(
        self, config: utils.DataIngestorConfig, reader_function: pd.DataReaderFunction
    ) -> NoReturn:
        super().__init__(config, reader_function)

    def create_directory(self, path: str) -> NoReturn:
        """
        Method for creating a directory in a local file storage.
        """
        path = os.path.join(self.config.data_path, path)
        logger.logger.info(f"Creating directory {path}")
        if not os.path.exists(path):
            os.makedirs(path)

    def list_files(self):
        """
        Method for listing files in a local file storage.
        """
        return os.listdir(self.config.data_path)


class S3DataIngestor(DataIngestor):
    """
    The data ingestor class designed to ingest the file from a S3 bucket into the pipeline.
    """

    def __init__(
        self, config: utils.DataIngestorConfig, reader_function: pd.DataReaderFunction
    ) -> NoReturn:
        super().__init__(config, reader_function)
        self.s3_client = boto3.client("s3")

    def create_directory(self, path: str) -> NoReturn:
        """
        Method for creating a directory in a S3 bucket.
        """
        logger.logger.info(
            f"Creating directory {path} in the {self.config.data_path} bucket.."
        )
        self.s3_client.put_object(Bucket=self.config.data_path, Key=path + "/")

    def list_files(self):
        """
        Method for listing files in a S3 bucket.
        """
        return self.s3_client.list_objects(Bucket=self.config.data_path)["Contents"]
