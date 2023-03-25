"""#1. Try tuple examples with list as well  * Hint: list can be defined using [] instead of ()
t1 = (123, "ABC", 'xyz', 3.14)     # uses paranthesis, different data types
print("t1 = ", t1)
"""
list1 = [123, "ABC", 'xyz', 3.14]
print("list1 = ", list1)


list2 = (123, "ABC", 123, 'xyz', 3.14, "ABC")      # duplicate values allowed
print("list2 = ", list2)

list3 = (10, 20, 30, 40, 20, 15)
print("list3 = ", list3)

# challenges for t2
# print first element
print("first elemen of list2t: ", list2[0])

# print last element
print("last elementof list2:", list2[-1])

# print values without using loop or multiple statements "ABC", 123, 'xyz', 3.14
print("slicing: ", list2[1:5])

list4 = [10, 20, 30, 40, 20, 15, (1, 2, 3)]
print("last element of list4: ", list4[-1])
print("second element of sub tuple", list4[-1][1])

#2. define a tuple t5 and a list l5 with following 5 elements and print it:
list5=[10, 20, [30, 40], 20, (1, 2, 3)]
print("list5=",list5)

#3. for list list5 in Q2:
#A. Try to modify the value 10 to 5 (Print value before and after modification). and note down the observation. 
#list[ 0]=5
#TypeError: 'type' object does not support item assignment
list5[0] = 5
print("1:",list5[0])
#B. Try to modify the value 30 to 45 (Print value before and after modification). and note down the observation.
list5[2][0]=45
print("2:",list5[2])
#C. Try to modify the value 2 to 24 (Print value before and after modification). and note down the observation. """
list5[4][1] = 24
print("3=", list5)

#D. Print the length (number of elements)
print(len(list5))

#E. Print it in reverse sequence, without using loops or methods (hint: use slicing)
print(list5[::-1])

#F. print it in sorted order using built-in method.
print(list5.sort())
#G. print it in reverse sorted order using built-in method.
print(type(list5.sort(reverse=True)))
#H. Print its type and note down the observation

#4. for list l5 in Q2:
#A. Try to modify the value 10 to 5 (Print value before and after modification). and note down the observation.
#B. Try to modify the value 30 to 45 (Print value before and after modification). and note down the observation.
#C. Try to modify the value 2 to 24 (Print value before and after modification). and note down the observation.
#D. Print the length (number of elements)
#E. Print it in reverse sequence, without using loops or methods (hint: use slicing)
#F. print it in sorted order using built-in method.
#G. print it in reverse sorted order using built-in method.
#H. Print its type and note down the observation

#5. Try following code and note down the observations:
t6 = 1, 2, 3
print(type(t6))

#6. Try following code and note down the observations:
t7 = ()
#print type and length of t7
print(type(t7),len(t7))

#7. Try following code and note down the observations:

t8 = (10)
#print type and length of t8
print(type(t8))    #int
#print(len(t8))    #File "<string>", line 61, in <module>
#TypeError: object of type 'int' has no len()

t9 = (10,)
#print type and length of t9
print(type (t9))    #tuple
print(len(t9))

t10 = ("Am I a tuple?")
#print t10, type and length of t10
print(type(t10))    #int
#print(len(10))
#File "<string>", line 72, in <module>
#TypeError: object of type 'int' has no len()


t11 = ('I am a tuple with single value',)
#print t11, type and length of t11
print(type(11))    # int
#print(len(11))
# File "<string>", line 80, in <module>
#TypeError: object of type 'int' has no len()

t12 = ("hello", "world")
print(type(t12))
print(len(t12))

#8. Check if there is any method, to remove an element from the end (in case of multiple)

# no



#9. Write a program to remove second occurence of a number from the list (in case of multiple).
"""
list =[1,2,3,4,1,2,4,8,2,4]
print(list)
list.remove(1)
list.remove(1)
print(list)
# remove all occurences
val=4
while val in list:
    list.remove(val)

print(list)

#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
str = input("give comma separated nos")
slist = str.split(',')
print(slist)

stuple  =tuple(str.split(','))
print(stuple)


#3. Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]

print(color_list[0], color_list[-1])"""