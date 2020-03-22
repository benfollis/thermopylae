# A dummy thermometer that can be used to test the rest server. Returns -274.00, which is below absolute zero

class Dummy:

    def __init__(self):
        pass

    def read(self):
        return -274.00
