import random

class Student:
    
    def __init__(self, name, surname, city, age):
        self.name = name
        self.surname = surname
        self.city = city
        self.age = age
        self.schoolname = None
        self.fieldOfStudy = None
    
    def printData (self):
        print(self.name, self.surname, self.city, self.age, self.schoolname, self.fieldOfStudy, self.country)

    def addCountry (self, country):
        self.country = country

student1 = Student("Kasia" , "Wrona" , "Cracow" , 20)
student1.country = "Poland"
student1.printData() # Kasia Wrona Cracow 20 None None Poland

class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentsList = []
        self.fieldOfStudy = ["Math" , "English" , "IT" , "Robotics"]

    def addStudent (self, student):
        if isinstance(student, Student):
            self.studentsList.append(student)
            student.schoolname = self.name
            student.fieldOfStudy = random.choice(self.fieldOfStudy)

    def PrintSchoolInfo (self):
        print ("School name: " , self.name , "city: " , self.city)
        print ("Students: ")
        for el in self.studentsList:
            el.printData()


student2 = Student("Zbigniew" , "Chmura" , "Warsaw" , 21 )
student2.country = "Poland"

school1 = School("Techs" , "Cracow")
school1.addStudent (student1)
school1.addStudent (student2)
school1.PrintSchoolInfo ()

    

            