
class Vehicle:
    def __init__ (self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 157
        self.numWheels = 4

    def printVehicleInfo (self):
        print ("Vehicle info: " , self.brand, self.name, self.topSpeed, self.numWheels)

vehicle1 = Vehicle("Japan Motors" , "name unknown")
vehicle1.printVehicleInfo() # Vehicle info:  Japan Motors name unknown 157 4

class Car (Vehicle):


    def printCarInfo (self):
        self.topSpeed = 231 #atribute in car1 object below (top speed) is executed from the class Car.
        print("Car info:" , self.name, self.brand , self.topSpeed, self.numWheels)
    
    def printVehicleInfo(self):
    
        print("Car.printVehicleInfo: " , self.brand, self.name, self.topSpeed, self.numWheels)


car1 = Car ("Toyota" , "Camry")
car1.printCarInfo () # Car info: Camry Toyota 231 4
car1.printVehicleInfo() # Car.printVehicleInfo:  Toyota Camry 231 4 
# the previous method - printVehicleInfo from class Vehicle was replaced by the one from the class Car.


class SuperCar(Car):

    def reachSpeed300 (self):
        self.topSpeed = 317
        print ("super car reached 300!")


superCar1 = SuperCar ("Nissan" , "460z")

superCar1.reachSpeed300() # super car reached 300! # method executed
superCar1.printVehicleInfo() # Car.printVehicleInfo:  Nissan 460z 317 4

