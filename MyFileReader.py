from FileReaderInterface import FileReaderInterface
from contextlib import contextmanager

class MyFileReader(FileReaderInterface):
    @contextmanager
    def read_file(self, file_name: str, buffer_size: int):
        """
        Тут типа манагер контекста, пытаемся читать файл
        """
        try:
            file = open(file_name, 'r', buffering=buffer_size)
            yield self._read_chunks(file, buffer_size)
        except Exception as e:
            raise e
        finally:
            file.close()
    
    def _read_chunks(self, file, buffer_size):
        """
        Тут типа генерим функцию для чтения файла
        Generator function to read file in chunks
        """
        while True:
            chunk = file.read(buffer_size)
            if not chunk:
                break
            yield chunk
