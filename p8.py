class Person:
    def info(self):
        print("I am a person")

class Teacher(Person):
    def role(self):
        print("I am a Teacher")

class Student(Person):
    def role(self):
        print("I am a Student")

t = Teacher()
s = Student()

t.info()
t.role()

s.info()
s.role()
