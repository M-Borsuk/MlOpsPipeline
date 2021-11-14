from dataclasses import dataclass


@dataclass
class DataDownloaderConfig:
    """Base configuration dataclass for DownloadDataIngestors."""

    download_url: str
    output_path: str

@dataclass
class DataIngestorConfig:
    """Base configuration dataclass for DataIngestors."""

    input_path: str
    output_path: str

@dataclass
class KaggleConfig(DataDownloaderConfig):
    """Configuration dataclass for kaggle related datasets"""

    user_name: str
    api_key: str
