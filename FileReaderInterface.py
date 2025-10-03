from abc import ABC, abstractmethod
from contextlib import contextmanager


class FileReaderInterface(ABC):
    @abstractmethod
    @contextmanager
    def read_file(self, file_name: str, buffer_size: int):
        """"generate buffer file reader"""
        pass
