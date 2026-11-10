from abc import ABC, abstractmethod
class Patient:
    def __init__(self,name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        print(self.__name)

    def set_name(self, name: str):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: float):
        if bill_amount < 0:
            print("Bill amount cannot be negative.")
        else:
            self.__bill_amount = bill_amount

    def calculate_bill(self):
        print(f"Original Bill Amount: {self.get_bill_amount()}")
        print(f"Final Bill Amount: {self.get_bill_amount()}")

    def displayPatientType(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        print(f"Original Bill Amount: {self.get_bill_amount()}")
        print(f"Final Bill Amount: {self.get_bill_amount() - (self.get_bill_amount() * 0.20)}")

    def displayPatientType(self):
        print("Patient Type: Senior Patient")

class PhilHealthPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)
    
    def calculate_bill(self):
        print(f"Original Bill Amount: {self.get_bill_amount()}")
        print(f"Final Bill Amount: {self.get_bill_amount() - (self.get_bill_amount() * 0.15)}")

    def displayPatientType(self):
        print("Patient Type: PhilHealth Patient")

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
pHsens.get_reading()

tempSens = TempSensor()
tempSens.get_reading()

my_sensor = Sensor() #error: cant instantiate

juan = Patient("Juan Dela Cruz", 15000.00)
print("\n")
juan.get_name()
juan.calculate_bill()
juan.displayPatientType()

maria = SeniorPatient("Maria Santos", 15000.00)
print("\n")
maria.get_name()
maria.calculate_bill()
maria.displayPatientType()

pedro = PhilHealthPatient("Pedro Reyes", 15000.00)
print("\n")
pedro.get_name()
pedro.calculate_bill()
pedro.displayPatientType()
