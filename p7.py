class Person:
    def __init__(self, name):
        self.__name = name   # private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

p = Person("Dhruvi")
print(p.get_name())

p.set_name("Lad")
print(p.get_name())
