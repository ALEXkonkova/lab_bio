from abc import ABC, abstractmethod


class CoderInterface(ABC):
    @abstractmethod
    def run(self, coder_info: str, string_to_process: str) -> str:
        """run code or decode function, base on coder_info"""
        pass

    @abstractmethod
    def _code(self, string_to_code: str) -> str:
        pass

    @abstractmethod
    def _decode(self, string_to_decode: str):
        pass
