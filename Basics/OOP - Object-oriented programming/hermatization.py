
class Vehicle:

    def __init__(self, name, brand):

        self.name = name
        self.brand = brand
        self.__owner = "'Fiat'"


    def __printVehicleData (self):           # hermetization 
        return "Owner: " + (self.__owner)

    def printInfo (self):
        print (self.name, self.brand, self.__printVehicleData())

    def printinfo2 (self):
        print(self.name, self.brand)


vehicle1 = Vehicle ( "500" , "Fiat" )
vehicle1.printInfo() # 500 Fiat Owner: 'Fiat'

print(vehicle1.name) # 500
# vehicle1.__printVehicleData() 
# # error - no access to the method


class Supercar(Vehicle):

    def __init__(self, name, brand, HP):
        
        self.HP = HP

        Vehicle.__init__ (self, name, brand)

    def printsuperCarData (self):
        print (self.brand, self.name, self.HP)    

Supercar1 = Supercar ("Enzo" , "Ferrrari" , 650)
Supercar1.printsuperCarData() # Ferrrari Enzo 650

Supercar1.printinfo2() # Enzo Ferrrari
Supercar1.printInfo() # Enzo Ferrrari Owner: 'Fiat'

# Supercar1.__printVehicleData()
# # the same error as above - AttributeError: 'Supercar' object has no attribute '__printVehicleData'
# # # The above methods - printinfo2, prininfo from the class 'Vehicle' can be used

# WORKAROUND:

print(Supercar1._Vehicle__owner)  # 'Fiat'
print(Supercar1._Vehicle__printVehicleData()) # Owner: 'Fiat'