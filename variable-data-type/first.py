print('Hello world')
print("my name is bharat","my age is 24")

# variables
name = "bharat"
age = 24
salary = 45000
print("my name is : ",name)
print("my age is : ",age)
print("my salary is : ",salary)

# sum two number
a = 10
b = 20
sum = a+b
print(sum)
# print(type(sum))

# Data Type
    # -> Integers
    # -> String
    # -> Float
    # -> Boolean
    # -> None

# Operators

# Arithmetic Operators
a = 5
b = 2

sum = a+b
sum = a-b
sum = a*b
sum = a/b
sum = a%b
sum = a**b # a^b
print(sum)

# relational operators
a = 50
b = 20
print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)


# Assignment Operators
num = 10
num += 10
print(num)


num = 10
num -= 10
print(num)


num = 10
num *= 10
print(num)



num = 10
num /= 5
print(num)


num = 10
num %= 5
print(num)


num = 10
num **= 5
print(num)

# Logical Operators

a = 50
b = 30
print(not False)
print(not (a>b))

val1 = True
val2 = True
print("AND operators: ",val1 and val2)
print("OR operators: ",(a==b) or (a>b))

# Type Conversion

a = 2
b = 4.25
sum = a+b
print(type(sum))

#
a = int("5")
b = 2.5
sum = a+b
print(type(a))
print(sum)


#
a = float("2")
b = 5.25
sum = a+b
print(sum)

#  
a = 3.14
a = str(a)
print(type(a))


# user input
# input("Enter your name: ")

# a = input("Enter your age: ")
# print(a)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a+b
print(sum)

#

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your name: "))

print(name)
print(age)
print(marks)