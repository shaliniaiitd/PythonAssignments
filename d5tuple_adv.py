t1 = (10, 25, 15, 30, 10, 20)
a= ( ),
print(type(a))
print(id(t1), type(t1))
print("tuple contents", t1)

print("Reversed object address", reversed(t1))
print("Tuple using Reversed object", tuple(reversed(t1)))
# print("List using Reversed object", list(reversed(t1)))

print("sorted - list format", sorted(t1))  # it won't change the tuple contents
print("descending order - list format", sorted(t1, reverse=True))  # it won't change the tuple contents
print("-"*40)
#
# print("tuple contents", t1)
# t2 = sorted(t1)     # t2 is a list
# print("sorted t2", t2)
# print("t2 is a", type(t2))  # this is a list
#
# print("Reversed object address", reversed(t1))
# print("Tuple using Reversed object", tuple(reversed(t1)))
#
# t3 = tuple(sorted(t1))      # t3 is a tuple
# print("sorted t3", t3)
# print("t3 is a", type(t3))   # t3 is a tuple
# print("descending order - tuple format", tuple(reversed(t3)))
# print("descending order - tuple format", tuple(sorted(t1, reverse=True)))
#
# t4 = tuple([5, 10, 15])
# # t4 = tuple((5, 10, 15))
# print("t4 using tuple function", t4)
#