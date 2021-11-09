import logging
from pathlib import Path
from logging.config import fileConfig


fileConfig(str(Path(__file__).resolve().parents[1] / "logging.ini"))
logger = logging.getLogger("dev")
