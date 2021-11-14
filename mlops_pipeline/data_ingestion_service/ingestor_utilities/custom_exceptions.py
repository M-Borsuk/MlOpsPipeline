from typing import NoReturn


class Error(Exception):  # pragma: no cover
    """Base class for other exceptions"""

    pass


class KaggleDownloadError(Error):  # pragma: no cover
    """Raised when the kaggle dataset is not downloaded"""

    def __init__(self, command: str, error_message: str) -> NoReturn:
        self.command = command
        self.error_message = error_message
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return "Command {0} did not work. The error message -> {1}".format(
            self.command, self.error_message
        )


class WrongConfigError(Error):  # pragma: no cover
    """Raised when the Config dataclass is not created"""

    def __init__(self, configuration: dict, error_message: str) -> NoReturn:
        self.configuration = configuration
        self.error_message = error_message
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return "The configuration {0} did not work.\
                The error message -> {1}".format(
            self.configuration, self.error_message
        )


class UnknownIngestorError(Error):  # pragma: no cover
    """Raised when the Ingestor type is not known"""

    def __init__(self, ingestor_type: str) -> NoReturn:
        self.ingestor_type = ingestor_type

    def __str__(self) -> str:
        return "Unknown ingestor type -> {0}".format(self.ingestor_type)
