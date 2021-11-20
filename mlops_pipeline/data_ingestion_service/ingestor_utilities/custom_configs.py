from dataclasses import dataclass, field
from typing import Dict, Any, Optional


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
    output_path: str


@dataclass
class S3DataIngestorConfig(DataIngestorConfig):
    """Configuration dataclass for S3DataIngestors."""

    s3_access_key: str
    s3_secret_key: str
    s3_region: str
    s3_bucket: str
    read_options: Optional[Dict[str, Any]] = field(default_factory=dict)
    write_options: Optional[Dict[str, Any]] = field(default_factory=dict)


@dataclass
class LocalFSDataIngestorConfig(DataIngestorConfig):
    """Configuration dataclass for LocalFSDataIngestors."""

    read_options: Optional[Dict[str, Any]] = field(default_factory=dict)
    write_options: Optional[Dict[str, Any]] = field(default_factory=dict)
