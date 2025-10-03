#!/usr/bin/env python3

import sys
from RLECoder import RLECoder
from ConfigException import ConfigException
from MyConfigReader import MyConfigReader
from MyFileReader import MyFileReader


class MainClass:
    def __init__(self):
        self._config_reader = MyConfigReader()
        self._file_reader = MyFileReader()
        self._coder = RLECoder()

    def run(self, config_file_name: str) -> str:
        result = ""
        try:
            configuration = self._config_reader.read_config(config_file_name)
            file_name = configuration[self._config_reader.file_name_for_coder_param_name]
            buffer_size = configuration[self._config_reader.buffer_size_param_name]
            coder_configuration = configuration[self._config_reader.coder_run_option_param_name]

            with self._file_reader.read_file(file_name, buffer_size) as chunks:
                for chunk in chunks:
                    chunk_res = self._coder.run(coder_configuration, chunk)
                    result += chunk_res
            return result

        except ConfigException as e:
            # Для автотеста возвращаем ошибку в stdout
            return str(e)
        except Exception as e:
            return f"Unexpected error: {str(e)}"

def test_main():
    import tempfile
    import os

    # Подготовка конфига
    config_content = """
    buffer_size = 10
    file_name = test.txt
    coder_option = code
    """
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as config_file:
        config_file.write(config_content)
        config_name = config_file.name

    test_content = "absfsddvsdvsdfsdfafaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    expected_result = "1a1b1s1f1s2d1v1s1d1v1s1d1f1s1d1f1a1f1a10a10a8a"
    with open('test.txt', 'w') as f:
        f.write(test_content)

    # Запуск
    main = MainClass()
    result = main.run(config_name)

    # Проверка
    assert result == expected_result

    # Очистка
    os.unlink(config_name)
    os.unlink('test.txt')


if __name__ == '__main__':
    # Читаем имя файла конфига из stdin
    test_main()
    config_file_name = sys.stdin.read().strip()
    main_class = MainClass()
    result = main_class.run(config_file_name)
    print(result, end='')
