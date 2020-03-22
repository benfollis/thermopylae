import json
from thermopylae.drivers.linuxgpio import LinuxGPIO
from thermopylae.drivers.dummy import Dummy


# Basic config binder.
# Names are case insensitive, and will be converted to python strings from
# unicode. Hence it's not recommended to use non-ASCII names
class ConfigBinder:

    def __init__(self, config_file_path):
        config_file = open(config_file_path, 'r')
        config_data = config_file.read()
        self.config = json.loads(config_data)

    def bind(self):
        # need the rest config
        bound_config = {'rest': self.config['rest']}
        thermometers = {}
        for thermometer in self.config['thermometers']:
            thermometers.update(self.__create_thermometer(thermometer))
        bound_config['thermometers'] = thermometers
        return bound_config

    def __create_thermometer(self, thermometer):
        name = thermometer['name']
        type = thermometer['type'].lower()
        print('Configuring thermometer ' + name + ' of type ' + type)
        driver = None
        if type == 'linux_gpio':
            driver = LinuxGPIO(thermometer['id'], thermometer['precision'])
        if type == 'dummy':
            driver = Dummy()
        if driver is None:
            raise Exception("Unknown thermometer type " + type)
        result = {name: driver}
        return result
