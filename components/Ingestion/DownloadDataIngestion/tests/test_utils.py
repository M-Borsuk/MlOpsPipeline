import pytest
from typing import Tuple, NoReturn, Dict
from pathlib import Path
from src.utils import Config, KaggleConfig, load_yaml


@pytest.mark.parametrize(
    "download_url,output_path,expected_result",
    [
        (
            "heesoo37/120-years-of-olympic-history-athletes-and-results",
            "/data/",
            ("heesoo37/120-years-of-olympic-history-athletes-and-results",
             "/data/"),
        )
    ],
)
def test_Config(
    download_url: str, output_path: str, expected_result: Tuple[str]
) -> NoReturn:
    config = Config(download_url, output_path)
    assert (config.download_url, config.output_path) == expected_result


@pytest.mark.parametrize(
    "download_url,output_path,user_name,api_key,expected_result",
    [
        (
            "heesoo37/120-years-of-olympic-history-athletes-and-results",
            "/data/",
            "user",
            "1911e2f17r8f1f3",
            (
                "heesoo37/120-years-of-olympic-history-athletes-and-results",
                "/data/",
                "user",
                "1911e2f17r8f1f3",
            ),
        )
    ],
)
def test_KaggleConfig(
    download_url: str,
    output_path: str,
    user_name: str,
    api_key: str,
    expected_result: Tuple[str],
) -> NoReturn:
    config = KaggleConfig(download_url, output_path, user_name, api_key)
    assert (
        config.download_url,
        config.output_path,
        config.user_name,
        config.api_key,
    ) == expected_result


@pytest.mark.parametrize(
    "download_url,output_path",
    [
        (
            "heesoo37/120-years-of-olympic-history-athletes-and-results",
            "/data/",
        )
    ],
)
def test_KaggleConfig_exception(
    download_url: str,
    output_path: str,
) -> NoReturn:
    with pytest.raises(Exception):
        KaggleConfig(download_url, output_path)


@pytest.mark.parametrize(
    "yaml_file,expected_result",
    [
        (
            str(Path(__file__).parent.joinpath("data/test_config_file.yaml")),
            {
                "download_url": "http://",
                "output_path": "http://",
                "user_name": "user",
                "api_key": "175f1735gv",
            },
        )
    ],
)
def test_load_yaml(
    yaml_file: str,
    expected_result: Dict[str, str]
) -> NoReturn:
    assert load_yaml(yaml_file) == expected_result
