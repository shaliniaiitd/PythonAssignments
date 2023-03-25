# # def greet():
# #     print("Hello")
#
#
# # main script
# name = "Sachin"
# greet(name)     # TypeError: greet() takes 0 positional arguments but 1 was given
#

# def greet(name):        # name is a prameter here
#     print("Hello", name)
#
#
# # main script
# name = "Virat"
# greet(name)     # passing the arguments
#
# -------------------------------------------
# def greet(name, income):
#     print("Hello", name)
#     print("Your income is", income)
#
#
# # main script
# name = "Sunil"
# # greet(name, 10000)     # passing the arguments
# # greet()     # error
# # greet(name)     # TypeError: greet() missing 1 required positional argument: 'income'
# # greet(name, 10000, 10)     # TypeError: greet() missing 1 required positional argument: 'income'
#
# greet(10000, "Dhoni")     # passing the arguments
# -------------------------------------------------------------

def greet(name, income, tax_rate):  # positional parameters
    print("Hello", name)
    print("Your income is", income)
    print("Your incometax is", (income * tax_rate) / 100)


# main script
name = "Sunil"
greet(name, 10000, 10)
# greet(10000, 10, "Anil")  # position of args
# greet(name, 10000)        # number of args

# Defining a function :: Positional arguments (check function call)
def greet(name, income, taxRate=20, taxPaid=True):
    print("Hello ", name)
    print("Your income is", income)
    print("Your incometax is", (income*taxRate)/100)
    if taxPaid:
        print("Tax is paid")
    else:
        print("Tax is not paid")

# function called with two argument.
# main script
# greet("Sunil", 20, 1000)
greet("Sunil", 1000, 20)

# --------------------------------------------------
# defining function with default argument


# def greet(name, income, taxRate=20):       # positional parameters
#     print("Hello", name)
#     print("Your income is", income)
#     print("Your incometax is", (income*taxRate)/100)
#
#
# # main script
# name = "Sunil"
# # greet(name, 10000, 10)
# # greet("Hrithik", 10000)
# greet("Kapil", 25000, 15)
#

# def greet(name, income, taxRate=20, taxPaid=True):       # positional parameters
#     print("Hello", name)
#     print("Your income is", income)
#     print("Your incometax is", (income*taxRate)/100)
#     if taxPaid:
#         print("Tax is paid")
#     else:
#         print("Tax is not paid")
#
#
#
# # main script
# name = "Sunil"
# # greet(name, 10000, 10)
# # greet("Hrithik", 10000)
# # greet("Kapil", 25000, 15)
# # greet("Harshad", 25000, 30, False)
# greet("Harshad", 25000, 30, True)


# # defining function with default param:: there cannot be a positional param after default param
# def greet(name, taxRate=20, income,  taxPaid=True):       # positional parameters
def greet(name, income, taxRate=20, taxPaid=True):       # positional parameters
    print("Hello", name)
    print("Your income is", income)
    print("Your incometax is", (income*taxRate)/100)
    if taxPaid:
        print("Tax is paid")
    else:
        print("Tax is not paid")



# main script
name = "Sunil"
# greet(name, 10000, 10)
# greet("Hrithik", 10000)
# greet("Kapil", 25000, 15)
# greet("Harshad", 25000, 30, False)
# greet("Harshad", 25000, 30, True)
# greet("Kapil", 30, 70000, True)
greet("Kapil", 30000)
greet("Kapil", 30000, 25)



# n1, n2: positional params
# n3: default param
# def add_numbers(n1, n2, n3=5, *args):  # here args is a tuple         #Note: * is imp here. var name can be anything
def add_numbers(n1, n2, n3=5, *n):  # here n is a tuple         #Note: * is imp here. var name can be anything
    sum1 = n1 + n2 + n3 + sum(n)
    # print(n[0])
    print(sum1)

# 0 extra args
add_numbers(3, 3)
add_numbers(3, 3, 1)

add_numbers(3, 3, 2, 4)     # 1 extra arg
add_numbers(3, 3, 2, 4, 4)     # 2 extra args
add_numbers(3, 3, 2, 4, 4, 34, 78, 12, 10)     # any number of extra args

t1 = (10, 20, 30, 12, 14)
add_numbers(1,2,3,4,*t1)  # any number of extra args * is imp
# add_numbers(1,2,3,4,t1)  # sent as a tuple directly.

# Defining a function :: Keyword arguments (check function call)
def greet(name, income, taxRate=20, taxPaid=True):
    print("Hello ", name)
    print("Your income is", income)
    print("Your incometax is", (income*taxRate)/100)
    if taxPaid:
        print("Tax is paid")
    else:
        print("Tax is not paid")

# function called with two argument.
# main script
# greet("Sunil", 20, 1000)
# greet("Sunil", 1000, 20)
# greet("Sunil", 1000, taxRate=20)  # keyword arguments
# greet("Sunil", 1000, taxRate=15)    # keyword arguments
# greet("Sunil", taxRate=15, income=1000)     # keyword arguments
# greet(name="Sunil", taxRate=15, income=1000)     # keyword arguments

# greet(True, name="Sunil", taxRate=15, income=1000)     # incorrect assignment of keyword arguments
# TypeError: greet() got multiple values for argument 'name'

# variable number of args with dictionary
# def add_numbers(n1, n2, n3=5, *args, **kwargs):     # here args is a tuple and kwargs is dictionary
def add_numbers(n1, n2, n3=5, *n, **num):     # here n is a tuple and num is dictionary
    sum1 = n1 + n2 + n3 + sum(n)
    print(num)
    print(n)
    print(sum1)


# add_numbers(1, 2, 7)
add_numbers(1, 2, 7, 4, 2, 45, 2, 5, a=6, b=10)   # 1 n1  2 n2  7 n3  4,2,45,2,5 *n  a=6, b=10 **num
# add_numbers(1, 2, 7, 4, 2, 45, 2, 5, a=6, b=10, 3, 2)   # Not allowed

# # if you give dictionary before tuple, it will not work
# def add_numbers(n1, n2, n3=5, **num, *n):     # here n is a tuple and num is dictionary
#     sum1 = n1 + n2 + n3 + sum(n)
#     print(num)
#     print(n)
#     print(sum1)

# ====================================================
# Passing List as a parameter
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


# main script
usernames = ['sunil', 'nitin', 'karan', 'ravi']
greet_users(usernames)


# All arguments in the Python language are passed by reference.

# # # ----------------------------------------------------------
# # # Immutable object as argument - Integer
# # # ----------------------------------------------------------
# def update(x):
#     print('Value of x ', x)
#     print('Memory Address of x before update', id(x))
#     x = 8
#     print('Value of x after update', x)
#     print('Memory Address of x after update', id(x))
#
#
# a = 10
# print('Value of a ', a)
# print('Memory Address of a before update', id(a))
# # a = 15
# # print('Value of a ', a)
# # print('Memory Address of a after modification', id(a))
# update(a)
# print('Value of a after update', a)
# print('Memory Address of a after update', id(a))


# # ----------------------------------------------------------
# # Mutable object as argument - List
# # ----------------------------------------------------------
def update(x):
    print('inside function, before update', x)
    print('Memory address of list inside function, before update', id(x))
    x[1] = 8
    print('inside function, after update', x)
    print('Memory address of list inside function, after update', id(x))


spam = [1, 2, 3]
print('Items in list', spam)
print('Memory address of list', id(spam))
# spam[1] = 5
# print('Items in updated list', spam)
# print('Memory address of updated list', id(spam))
update(spam)
print('Items in updated list', spam)
print('Memory Address of updated list', id(spam))

def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d     # packing
    # print("This line will not be reachable")

a = 5
b = 4
result1, result2 = add_sub(a, b)    # unpacking
print(result1)
print(result2)

# # a = 5
# # b = 7
# a, b = 5, 7