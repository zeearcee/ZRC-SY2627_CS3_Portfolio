from abc import ABC, abstractmethod
class Sensor(ABC):
    @abstractmethod
    def  get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        print("7.2 pH")  

class TempSensor(Sensor):
    def get_reading(self):
        print("24.5 °C")


pHsens = PHSensor()
tempSens = TempSensor()
my_sensor = Sensor()
pHsens.get_reading()
tempSens.get_reading() 

