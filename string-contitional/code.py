# strings

str1 = "this is string"
str2 = 'this is string'
str3 = """this is string"""
print(str1)
print(str2)
print(str3)

# Basic Operation

# concatenation (add two string)
s1 = "bharat "
s2 = "kumar"
finall_string = s1+s2
print(len(finall_string))

# indexing
str = "bharatkumar"
print(str[2])


# Slicing
st = "bharatkumar"
print(st[1:6])
print(st[:4]) #[0:4]
print(st[5:]) #[5:len(str)]


# Slicing
# Negative Index
s = "apple"
print(s[-3:-1])


# String Function
str = "i am a python student"
# print(str)

print(str.endswith("ent")) # last string mach 
print(str.capitalize()) # first letter captel
print(str.replace("python","javaScript")) # chnange string
print(str.find("e")) # character find
print(str.count("a")) # duplicate letter


# Conditional Statement
# if-elif-else Roles

age = 21

if(age>=18):
    print("Can vote & apply for license ")
else:
    print("Not eligible ")

    
