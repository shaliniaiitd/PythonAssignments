# age = input("Please enter your age: ")  # the value received using input() method is always String
# print(type(age))

# Single line comment
age = input("Please enter your age: ")  # the value received using input() method is always String
# use int() to convert it into integer format
print(type(age))

# Python does not
# support
# block level
# comments

str_value = "Welcome"

# This is the first usage of """""""
"""
This is multiline comment in python
Python does not
support
block level 
comments
"""


# This is the second usage of """""""  if you want to store multiline string in a variable
str_var = """
Python does not
support
block level 
comments
"""
print(str_var)

# print("Your age is " + age)  # works
print("Your age is", age)