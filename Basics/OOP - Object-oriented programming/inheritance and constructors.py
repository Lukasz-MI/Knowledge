
class Person:
    def __init__ (self, name, surname, age):

        self.name = name
        self.surname = surname
        self.age = age 
        
        self.printPersonData()

    def printPersonData (self) :
        print ("Class Person: " , self.name, self.surname, self.age)

class Employee(Person):

    def __init__ (self, name, surname, age, position, salary):
        self.position = position
        self.salary = salary
        Person.__init__(self, name, surname, age)
        self.EmployeeData()

    def EmployeeData (self):
        print("Employee class: " , self.name, self.surname , self.position, self.salary)

candidate1 =  Employee ("Zbyszek" , "Golebiowski" , 51 , "Construction Lead" , 11000)

# Both constructors are used, console results:

'''

 Class Person:  Zbyszek Golebiowski 51
 Employee class:  Zbyszek Golebiowski Construction Lead 11000

'''

print()
print()

class Manager (Employee):

    def __init__ (self, name, surname, age, position, salary , department):
        
        Employee.__init__(self , name, surname, age, position, salary)
        self.department = department
        self.printFullManagerData()

    def printFullManagerData (self):
        print ("Manager details: " , self.name, self.surname, self.age , self.position, self.salary , self.department)


manager1 = Manager ( "Henry" , "Farlier" , 57 , "Construction Projects Manager" , 23000 , "Construction Projects department") 

# All three constructors are used, console results:

'''

Class Person:  Henry Farlier 57
Employee class:  Henry Farlier Construction Projects Manager 23000
Manager details:  Henry Farlier 57 Construction Projects Manager 23000 Construction Projects department

'''
manager1.EmployeeData() # Employee class:  Henry Farlier Construction Projects Manager 23000
                        # Method used from class Employee

manager1.printPersonData() # Class Person:  Henry Farlier 57
                           # Method from class person

manager1.printFullManagerData() # Manager details:  Henry Farlier 57 Construction Projects Manager 23000 Construction Projects department
                                # Method from class Manager

