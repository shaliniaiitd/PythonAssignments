t3 = (40, 10, 25, 15, 30, 10, 20)

print("t3 contents ", t3, "t3 is a ", type(t3))
print("length of t3", len(t3))
print("first element", t3[0])
print("last element", t3[-1])
print("first 3 elements", t3[:3])
print("last 4 elements", t3[-4:])
print("Rev of t3", t3[::-1])
print("-"*40)

print("10 in t3", 10 in t3)
print("10 not in t3", 10 not in t3)
print("100 not in t3", 100 not in t3)
print("-"*40)

print("index of 10 in t3", t3.index(10))
print("count of 10 in t3", t3.count(10))
# print("index of 100 in t3", t3.index(100))  # value error when element not present in tuple

print("index of 100 in t3", t3.index(100) if 100 in t3 else "Not Found")  # value error when element not present in tuple
# shorthand of if (print its index if found else "not found"

t4 = t3
print("t3 == t4", t3 == t4)     # T         # Values are same
print("t3 is t4", t3 is t4)     # T         # ids are also same

t2 = (40, 10, 25, 15, 30, 10, 20)           # same values with same sequence
print("t3 == t2", t3 == t2)     # T         # Values are same
print("t3 is t2", t3 is t2)     # T         # ids are also same

t1 = (10, 40, 25, 15, 30, 10, 20)           # different sequence
print("t2 == t1", t2 == t1)     # F         # Values are different
print("t2 is t1", t2 is t1)     # F         # ids are also different

t6 = (40, 10, 25, 15, 30) + (10, 20)        # addition of tuples
# t6 = (40, 10, 25, 15, 30) * 2               # repetition of tuples is allowed
# t6 = (40, 10, 25, 15, 30) - (10, 20)          # - not allowed
print("t6", t6)
print("t3 == t6", t3 == t6)     # T         # Values are same
print("t3 is t6", t3 is t6)     # T         # ids are also same

t7 = (40, 10, 25, 15, 30)               # m1
t7 += (10, 20)                          # m2
print("t7", t7)
print("t3 == t7", t3 == t7)     # T         # Values are same
print("t3 is t7", t3 is t7)     # F         # ids are different

t8 = t7
print("t8 is t7", t8 is t7)     # T
print("t8 is t3", t8 is t3)     # F

print("first element", t7[0])
# t7[0] = 15


# str = "Sunil"
# print("first char", str[0])
# # str = "Bansal"
# # str += "Bansal"
# # str[0] = "B"

ts = (1, "Sachin", "Tendulkar", 2, "Rahul", "Dravid")
print("Tuple with different data types", ts)