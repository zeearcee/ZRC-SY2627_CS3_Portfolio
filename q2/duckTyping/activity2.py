class Car():
    def move(self):
        print("The car is driving on the road.")

class Boat():
    def move(self):
        print("The boat sails on the water.")

class Drone():
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)   
start_trip(boat) 
start_trip(drone) 
