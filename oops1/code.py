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

# 4. Polymorphism
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()
# 5. Encapsulation
class Bank:

    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print(self.__balance)

b = Bank()

b.show_balance()
# 6. Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

c = Car()
c.start()

# Real Project Type OOP Example
# Bank Management System
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "Deposited")

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(amount, "Withdrawn")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)

# Object
user1 = BankAccount("Bharat", 10000)

user1.deposit(5000)

user1.withdraw(3000)

user1.check_balance()

