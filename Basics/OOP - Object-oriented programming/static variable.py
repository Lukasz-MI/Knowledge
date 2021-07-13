
class Employee:
    'Employee class - gives employee name and his/her position on the list'

    numEmployees = 0    
    employeesList = []
    
    def __init__(self, name):
        self.name = name
        Employee.numEmployees +=1 # number will increas each time Employee class is used. Starting number is 0.
        print(self.name + ",", "number of employess:" , Employee.numEmployees)

        Employee.employeesList.append (self) # self here indicates on the object that we will be added to the list.

    def printData(self):
        print("Employee list:") 
        
        for el in Employee.employeesList:
            print(el.name) 

employee1 = Employee("Kate")
employee2 = Employee("Joanna")
employee3 = Employee("Brat")
employee4 = Employee("David")
employee5 = Employee("Kate")

print ("total number of employees:" , Employee.numEmployees)
print()

employee1.printData()

print(Employee.__doc__) # Employee class - gives employee name and his/her position on the list
print(Employee.__module__) # __main__
print(Employee.__name__) # Employee

print("name attr in Employee:" , hasattr(employee1 , "name")) # name attr in Employee: True
print("city attr in Employee:" , hasattr(employee1 , "city")) # city attr in Employee: False

employee1.city = "Lublin"
print("city attr in Employee:" , hasattr(employee1 , "city")) # city attr in Employee: True

print("Employee name:" , getattr(employee1 , "name")) # You should indicate the object and name of the atribute specified in the class constructor.
# Employee name: Kate

setattr(employee1, "name" , "Anne")
print ("New employee in place of Kate:" , getattr (employee1, "name")) # New employee in place of Kate: Anne
print(getattr(employee1 , "name")) # Anne

