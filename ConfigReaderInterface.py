from abc import ABC, abstractmethod


class ConfigReaderInterface(ABC):
    def __init__(self):
        self.buffer_size_param_name = "buffer_size"
        self.file_name_for_coder_param_name = "file_name"
        self.coder_run_option_param_name = "coder_option"

        self._param_delimiter = "="

        self._config_dict = \
            {
                self.buffer_size_param_name: None,
                self.file_name_for_coder_param_name: None,
                self.coder_run_option_param_name: None
            }

    @abstractmethod
    def read_config(self, config_file_name: str) -> dict:
        """"
        coder_option can be only "code" or "decode"

        config_dict:return

        ConfigException:raise
        """
        pass
