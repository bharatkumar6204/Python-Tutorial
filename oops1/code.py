# 1. Class aur Object
# class
class Student:
    name = "bharat"

# object
s1 = Student()
print(s1.name)


# 2. Constructor (init)

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s2 = Student("bharat",23)
print(s2.name, s2.age)

# 3. Inheritance
class Father:
    def house(self):
        print("Father has house")

class Son(Father):
    def Son(self):
        print("Son has Car")
s = Son()

s.house()
s.Son()