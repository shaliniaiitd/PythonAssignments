import copy

l1 = [10, 25, [40, 12], 10, 40, 80, 20]
print("l1", l1)
# ----------------------------------

# l1.append([10,20])
# print("l1", l1)
#
# l0 = l1
# print("l0 == l1", l0 == l1, "l0 is l1", l0 is l1)   # T T
# print("l0 id", id(l0), "l1 id", id(l1))
#
# l0[1] = 35
# print(l1)   #  [10, 25, [40, 12], 10, 40, 80, 20]       [10, 35, [40, 12], 10, 40, 80, 20]
#
l
#
# l1[1] = 45
# print(l0)       # 25 or 35 or 45
# ==============================================
print("\ncopy: Shallow Copy")

l2 = l1.copy()  # does shallow copy
# l2 = copy.copy(l1)  # does shallow copy

print("l2", l2)
print("\nl2 == l1", l2 == l1, "l2 is l1", l2 is l1)
print("l2 id", id(l2), "l1 id", id(l1))

l1[1] = 35
l2[0] = 5
print(l1)
print(l2)

l1[2][0] = 50
print(l2[2][0])   # 50

# ==============================================
print("\ncopy: deep Copy")

l3 = copy.deepcopy(l1)  # deep copy - elements are copied recursively

print("l3 == l1", l3 == l1, "l3 is l1", l3 is l1)   # T F
print("l3 id", id(l3), "l1 id", id(l1))

print(id(l2[2]))
print(id(l3[2]))

l1[2][0] = 80
print(l3[2][0])  # not 80