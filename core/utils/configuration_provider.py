import json

class ConfigurationProvider:
    def __init__(self, config_file: str = "config/config.json") -> None:
        self._config_file = config_file
        self.config = self.__load_config_file()

    def __load_config_file(self) -> None:
        with open(self._config_file, "r") as file:
            config = file.read()
        return json.loads(config)
        
    