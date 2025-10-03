from ConfigReaderInterface import ConfigReaderInterface
from ConfigException import ConfigException

class MyConfigReader(ConfigReaderInterface):
    def read_config(self, config_file_name: str) -> dict:
        """
        Читает файл конфига и возвращает словарь с параметрами.
        Если buffer_size некорректный, используется дефолт 10.
        """
        # словарь с дефолтами
        self._config_dict = {
            self.buffer_size_param_name: 10,  # дефолтный buffer_size
            self.file_name_for_coder_param_name: None,
            self.coder_run_option_param_name: None
        }

        try:
            with open(config_file_name, 'r') as file:
                for line_number, line in enumerate(file, 1):
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue

                    if self._param_delimiter not in line:
                        raise ConfigException(
                            f"Неверный формат в строке номер {line_number}: '{line}'"
                        )

                    key, value = line.split(self._param_delimiter, 1)
                    key = key.strip()
                    value = value.strip()

                    if key == self.buffer_size_param_name:
                        try:
                            self._config_dict[key] = int(value)
                        except ValueError:
                            self._config_dict[key] = 10  # fallback silently

                    elif key == self.file_name_for_coder_param_name:
                        self._config_dict[key] = value

                    elif key == self.coder_run_option_param_name:
                        if value not in ['code', 'decode']:
                            raise ConfigException(
                                f"Неверный режим в строке номер {line_number}: '{value}'. "
                                f"Должен быть 'code' или 'decode'"
                            )
                        self._config_dict[key] = value

                    else:
                        raise ConfigException(
                            f"Неверный параметр в строке номер {line_number}: '{key}'"
                        )

            # проверка обязательных параметров
            for param_name, param_value in self._config_dict.items():
                if param_value is None:
                    raise ConfigException(f"Пропущен параметр: '{param_name}'")

            return self._config_dict.copy()

        except FileNotFoundError:
            raise ConfigException(f"Не обнаружен файл конфига: '{config_file_name}'")
        except ConfigException:
            raise
        except Exception as e:
            raise ConfigException(f"Ошибка чтения файла конфига: {str(e)}")