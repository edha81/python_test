from Person import person
class Student(person):
    def __init__(self,name,age,school):
        self.name =name
        self.age = age
        self.school = school

    def print_school(self):
        print(self.school)

