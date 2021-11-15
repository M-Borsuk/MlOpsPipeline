from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class DataDownloaderConfig:
    """Base configuration dataclass for DownloadDataIngestors."""

    download_url: str
    output_path: str


@dataclass
class KaggleConfig(DataDownloaderConfig):
    """Configuration dataclass for kaggle related datasets"""

    user_name: str
    api_key: str


@dataclass
class DataIngestorConfig:
    """Base configuration dataclass for DataIngestors."""

    input_path: str
    read_options: Dict[str, Any]
    write_options: Dict[str, Any]


@dataclass
class S3DataIngestorConfig(DataIngestorConfig):
    """Configuration dataclass for S3DataIngestors."""

    s3_access_key: str
    s3_secret_key: str
    s3_region: str
    s3_endpoint_url: str


@dataclass
class LocalFSDataIngestorConfig(DataIngestorConfig):
    """Configuration dataclass for LocalFSDataIngestors."""

    # No configuration needed for now for LocalFSDataIngestors.
    pass
