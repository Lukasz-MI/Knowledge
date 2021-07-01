
class Car:
    def __init__(self, brand, name, color, year):   # Każda metoda: np. __init__ musi zawierać self.
        self.brand = brand                           # self. zapewnia dostęp do wszystkich zmiennych (atrybutów wewnątrz obiektu). 
        self.name = name
        self.color = color
        self.year = year
        self.mileage = 1
        self.setFuelUse(0)
        self.printInfo()
        
    def setFuelUse (self, Fueluse):
            self.FuelUsage = Fueluse 

    def printInfo (self):
        print(self.brand, self.name, self.color, self.year, self.mileage, self.FuelUsage)

       
mustang = Car ("Ford" , "Mustang" , "red" , 1968)
mustang.FuelUsage = 14
mustang.printInfo()

bravo = Car ("Fiat" , "bravo II" , "blue" , 2010)
bravo.mileage = 100000
bravo.TopSpeed = 210
bravo.FuelUsage = 9.5
bravo.printInfo() 
print (bravo.TopSpeed)


print (type(bravo)) # <class '__main__.Car'>