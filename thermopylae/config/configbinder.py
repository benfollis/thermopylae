import json
from thermopylae.busdrivers.linuxgpio import LinuxGPIO

# Basic config binder.
# Names are case insensitive, and will be converted to python strings from
# unicode. Hence it's not recommended to use non-ASCII names
class ConfigBinder:

    def __init__(self, config_file_path):
        config_file = open(config_file_path, "r")
        config_data = config_file.read()
        self.config = json.loads(config_data)
        self.thermometers= {}

    def bind(self):
        self.bound_config = {"thermometers" : {}}
        for thermometer in self.config["thermometers"]:
            self._create_thermometer(thermometer)
        return self.bound_config
        
    def _create_thermometer(self, thermometer):
        if thermometer["type"].lower() == "linux_gpio":
            linux_gpio = LinuxGPIO(thermometer["id"], thermometer["precision"])
            self.thermometers[thermometer["name"]] = linux_gpio
