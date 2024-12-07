class Student:
    def __init__(self,name):
        self.name = name
        self.progress = 0
        self.energy = 50


student = Student("Nikita")

print (student.name)
student1 = Student("Alex")

student1.progress = 20

print(student1.name, student1.progress)
        
