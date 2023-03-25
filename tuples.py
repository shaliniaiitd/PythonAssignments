# Tuples
# Immutable
# can contain same or  different objects
# allows duplicates
# indexing: positive index     negative index
# supports sliciing
# inner tuple
# use parentheses   ()
# possible to define with or without using parentheses
# recommended to define or use with parentheses
# without parentheses: packing, unpacking

# t1 = (123, "ABC", 'xyz', 3.14)      # uses parentheses, different data types
# print("t1 = ", t1)

# t2 = (123, "ABC", 123, 'xyz', 3.14, "ABC")      # duplicate values allowed
# print("t2 = ", t2)
#
# t3 = (10, 20, 30, 40, 20, 15)
# print("t3 = ", t3)
#
# # challenges for t2
# # print first element
# print("first element: ", t2[0])
#
# # print last element
# print("last element: ", t2[-1])
#
# # print values without using loop or multiple statements "ABC", 123, 'xyz', 3.14
# print("slicing: ", t2[1:5])
#
# t5 = (11, 12)
# t4 = (10, 20, 30, 40, 20, 15, (1, 2, 3), t5)
# print("last element of tuple: ", t4[-1])
# print("second element of sub tuple", t4[-1][1])
#
# # ----------------------------------------------
# print(1, 2, 3)
#
# tup = (13, 245, 234)
# a = 1, 2, 3             # packing
# #
# v1 = 10
# v2 = 20
# v3 = 30
# b = v1, v2, v3, "Arpit"           # packing
# b = v1, v3, 10, 40
# # b[1] = 50     # not possible. as tuples are immutable
# #
# print(type(a))
# print(a)
# print(type(b))
# print(b)
#


# tup = (13, 245, 234)
# p, q, r = tup

a1 = 20
# p, q, r = 10, 20, 30
p, q, r = 10, a1, 30
print(type(p))
print(p)
#
# # v1 = 10
# # v2 = 20
# # v3 = 30
# # b = v1, v2, v3           # packing
#
# # p, q, r = b         # unpacking     b contains 10, 20, 30
# # p, q, r, str = b         # unpacking     b contains 10, 20, 30, str
# p, q, str, r = b         # unpacking     b contains 10, 20, 30, "Arpit"         number of values in tuple and number of var on LHS should match
# print(type(p))
# print(p)
# print(q)
# print(type(str))
# print(str)
# print(type(r))
# print(r)