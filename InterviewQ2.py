# num = input("number:")
# if (num == num[-1: : -1]):
#     print ("palindrome")
# else:
#     print ("No palindrome")

##---------------------------------------------------------

#Factorial
# num = int(input("number"))
#
# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         return n* factorial(n-1)
#
# # call
# print (factorial(num))
#------------------------------------------------------------

#Armstrong number

# num = input("number")
#
# sum = 0 ; l = len(num)
# for dg in num:
#     sum += int(dg)**l
#
# if sum == int(num):
#     print("Armstrong number")
# else:
#     print ("no armstrong")
#_______________________________________________________________

# #Bubble sort
#
inList = [50,20,6,103,67,2,9]
for j in range(0,len(inList)-2):
     if inList[j-1] < inList[j]:
         inList[j-1],inList[j] = inList[j],inList[j-1]
     j += 1
print(inList)
# #_____________________________________________________________________
#
# inStr = "I love my Company"
# ostr = ""
# print(inStr[: : -1])
# l = inStr.split(" ")
# for word in l:
# #     lw = list(word)
# #     lw[0] = lw[0].capitalize()
# #     lw[-1] = lw[-1].capitalize()
# #     for l in lw:
# #         ostr = ostr + l
# #     ostr = ostr + " "
# # print(ostr)
#

#
# instr = "internationalization"
# ostr = ""
# for letter in set(instr):
#     if (instr.count(letter) >1):
#         ostr = ostr + letter + "-" + str(instr.count(letter)) + ","
#
# print(ostr)
#

#19.
# instr = "aaabbcdddd"
# ostr = ""
# for letter in set(instr):
#
#          ostr = ostr + letter + str(instr.count(letter))
#
# print(ostr)
#__________________________________________________________________________________________________

# 15) Selection Sort
#
# Write a Python program to sort an array elements using selection sort algorithm.
#
# Input: 16,37,4,45,9,78,92
#
# Output: 4,9,16,37,45,78,92
#
# def min(l):
#     min =l[0]
#     for i in range(1,len(l)):
#         if l[i] < min:
#             min = l[i]
#
#     return min
#
# lunsort = [16,37,4,45,9,78,92]
# lsort = []
# while lunsort:
#     num = min(lunsort)
#     lsort.append(num)
#     lunsort.remove(num)
# print(lsort)

#
# 16) Insertion Sort
#
# Write a Python program to sort an array elements using insertion sort algorithm.
#
# Input: 15 6 30 2 50 28
#
# Output: 2 6 15 28 30 50

#Reverse Each Word in Sentence using Python
inpt = "This is a sentence."
print(inpt[::-1])
rvr = list(map(lambda x: x[::-1],inpt.split(" ")))

print(rvr)

