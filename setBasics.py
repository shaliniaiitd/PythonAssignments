# set
# unordered collection of elements with no duplicate elements
# membership can be checked
# supports mathematical operations like union, intersection, difference, and symmetric difference
# mutable

# can be defined using {} or using set() function
# Note: to create an empty set, we must use set(), not {}
# b'cos {} will give you an empty dictionary
# it does not support indexing, as unordered items has no index

# basket = {'apple', 'orange', 'apple', 'mango', 'kiwi', 'orange'}
# print(basket) # duplicates will be printed only once      # order can be anything

# basket = set(['apple', 'orange', 'apple', 'mango', 'kiwi', 'orange'])
# print(basket) # duplicates will be printed only once      # order can be anything

# print("orange in basket", 'orange' in basket)   # True
# print("watermelon in basket", 'watermelon' in basket)   # False
# print("banana not in basket", 'banana' not in basket)   # True
# print("-"*45)

# # single words
# a = set('abracadabra')
# b = set('alacazam')
# print("a", a)   # unique letters in a       # a {'c', 'b', 'd', 'r', 'a'}
# print("b", b)   # unique letters in b       # b {'c', 'z', 'm', 'l', 'a'}
#
# print("letters in a but not in b: a - b", a - b)  # difference
# # {'b', 'd', 'r'}
# # Explanation
# # x = 15
# # y = 10
# # print(x - y)
#
# print("letters in a or b or both: a | b", a | b)  # union
# # 'l', 'b', 'm', 'r', 'd', 'z', 'a', 'c'}
#
# print("letters in both a and b: a & b", a & b)  # Intersection
#
# print("letters in a or b but not in both: a ^ b", a ^ b)  # symmetric_difference
# # a {'a', 'b', 'c', 'd', 'r'}
# # b {'a', 'c', 'm', 'l',  'z'}
# # b, d, r, m, l, z
# print("-"*45)

veggies = {"cucumber", "broccoli", "tomato"}
print("veggies", veggies)

# add single element
veggies.add("beetroot")
print("veggies", veggies)   # position of beetroot can be anything
#  {'beetroot', 'cucumber', 'broccoli', 'tomato'}

# add multiple elements
veggies.update(["lettuce", "eggplant", "cauliflower"])
print("veggies", veggies)
# {'eggplant', 'cucumber', 'lettuce', 'cauliflower', 'tomato', 'broccoli', 'beetroot'}

print("length of veggies", len(veggies))

veggies.remove("lettuce")
# print(veggies.remove("lettuce"))       # None
print("veggies", veggies)

# print(veggies.remove("apple"))    #  KeyError: 'apple'
# print("veggies", veggies)

veggies.discard("apple")
print("veggies", veggies)
# veggies.discard("beetroot")
# print("veggies", veggies)

print(veggies)  # set without the removed veggie
last_item = veggies.pop()
print(last_item)    # one of the veggies
print(veggies)  # set after removing a random veggie

# emptying the set
veggies.clear()
print("veggies after clear", veggies)

# # deleting the set
# del veggies
# print("veggies after delete", veggies)  # NameError: name 'veggies' is not defined

# # joinining two sets
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# veggies = {"cucumber", "broccoli", "tomato"}
#
# union_ex = basket.union(veggies)  # will exclude duplicate items
# print("Union", union_ex)
# print("basket", basket)
#
# mix_them = basket.update(veggies)
# print("returned value", mix_them)
# print("basket including veggies", basket)

# print(basket[0])    # indexing not allowed      TypeError: 'set' object is not subscriptable
eSet = {}
print(type(eSet))   # dictionary

s4 = {1, 2, 5, (22, 11, 33)}        # tuple is allowed
print(s4)

# s5 = {1, 2, 5, [22, 11, 33]}        #  TypeError: unhashable type: 'list'
# print(s5)

# s6 = {1, 2, 5, {22, 11, 33}}        #  TypeError: unhashable type: 'set'
# print(s6)
