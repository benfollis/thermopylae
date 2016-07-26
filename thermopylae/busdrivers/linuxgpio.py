# This class reads the temperature data by traversing the /sys/bus/w1/devices subtrees looking for the thermometer
# specified. If the thermometer is found, it's value in C is returned.
#If the thermometer is not found a None reading is returned
import os.path

class LinuxGPIO:

    # target_thermometer: the linux name for the thermometer. E.G: 28-8000000476c9
    # precision: how many digits to the right of the decimal place is the thermometer cabple of
    def __init__(self, target_thermometer, precision):
        self.target_thermometer = target_thermometer
        self.divisor = 10 ** precision

    def read(self):
        thermometer_file = os.path.join('/', 'sys', 'bus', 'w1', 'devices', target_thermometer, 'w1_slave')
        if !os.path.exists(thermometer_file):
            return None
        with open(thermometer_file), 'r') as fh:
            reading = fh.read
        # to read find the string "t=" and read to end of file.
        temp_start = reading.index('t=')
        temp_raw = reading[temp_start + 2:].strip()
        temp = float(temp_raw)/divisor
        return temp

        
        
