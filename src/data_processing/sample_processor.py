# User module imports
import constants as c

# Python module imports
import pickle
from pathlib import Path
from typing import Self, Any, TypeVar, Type
from hashlib import md5

T = TypeVar("T", bound="ConfigLoadable")


class ConfigLoadable:
    """
    Class template to store and load class instances, as defined by its member variables.
    """

    def __init__(self: Self, /, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def from_config(cls: Type[T], config_path: Path | str) -> Self:
        """
        Initialize an instance using a config file path.
        """
        with open(config_path, "rb") as f:
            configs = pickle.load(f)
        return cls(**configs)

    def get_config(self: Self) -> dict:
        """
        Get the configuration of the class instance.
        """
        return self.__dict__

    def save_config(self: Self, config_filepath: Path | str) -> None:
        """
        Save the config of the class instance to a file.
        """
        with open(config_filepath, "wb") as f:
            pickle.dump(self.get_config(), f)


class SampleProcessor(ConfigLoadable):
    def __init__(
        self: Self,
        processed_files: set[str] | None = None,
        **kwargs,
    ) -> None:

        self.processed_files = processed_files or set()

        super().__init__(**kwargs)

    # --------------------------------------------------------------------
    # Data Lake communication

    def get_raw_file_from_data_lake(self: Self, filepath: str) -> dict:
        """
        Retrieve a raw file from the data lake using its file path.
        """
        # TODO: implement
        return {}

    def get_files_in_data_lake(self: Self) -> list[str]:
        """
        Get a list of all files present in the data lake.
        """
        # TODO: implement
        return []

    def get_unprocessed_files_in_data_lake(self: Self) -> list[str]:
        """
        Get a list of all unprocessed files in the data lake.
        """
        # TODO: implement
        return []

    # --------------------------------------------------------------------
    # File Processing

    def process_single_file(self: Self, filepath: str) -> None:
        """
        Process a single file from the data lake, refered to by its file path.
        """
        # TODO: implement
        return

    def update_database(self: Self) -> None:
        """
        Check all files in the data lake and process files that are not yet present in the database.
        """
        return

    # --------------------------------------------------------------------
    # Hashing and storage functions

    def _get_hash(self: Self, filename: str) -> str:
        return md5(filename.encode()).hexdigest()

    def mark_as_processed(self: Self, filename: str) -> None:
        self.processed_files.add(self._get_hash(filename))

    def is_processed(self: Self, filename: str) -> bool:
        return self._get_hash(filename) in self.processed_files

    # --------------------------------------------------------------------
    # Config saving and loading

    def save(self: Self) -> None:
        """
        Save to the default data processor config file path.
        """
        self.save_config(c.DATA_PROCESSOR_CONFIG_PATH)

    @classmethod
    def load(cls) -> Self:
        """
        Load from the default data processor config file path.
        """
        return cls.from_config(c.DATA_PROCESSOR_CONFIG_PATH)
