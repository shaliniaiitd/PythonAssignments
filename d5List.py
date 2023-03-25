 # Lists
 # mutable
 # can contain same or  different objects
 # allows duplicates
 # indexing: positive index     negative index
 # supports sliciing
 # inner list
 # use square brackets

listOne = [10, 20, "Manisha"]
listOne[0] = 50
print(listOne)          # [50, 20, 'Manisha']

listOne.append(100)        # single element e.g. int
print(listOne)          # [50, 20, 'Manisha', 100]
#
l2 = [500]
listOne.extend(l2)          # sequence e.g. a list
print("HERE",listOne)          # [50, 20, 'Manisha', 100,500]
#
l3 = [700, 800]
l4 = [250, 350]
listOne.append(l3)          # [50, 20, 'Manisha', 100, [700, 800]]  # we can mention a list as well which will get appended as an inner list
print(listOne)
listOne.extend(l4)          # [50, 20, 'Manisha', 100, 500, [700, 800], 250, 350]
print(listOne)

# # [50, 40, 20, 'Manisha', 100, 500, [700, 800], 250, 350]
listOne.insert(1, 100)
print(listOne)
listOne.insert(0, "Jyoti")  # ['Jyoti', 50, 100, 20, 'Manisha', 100, 500, [700, 800], 250, 350]
print(listOne)

listOne.insert(1, l3)   # append (as a inner list)    extend (as a normal element)
print(listOne)
# # ["Jyoti", [700, 800], 50, 100, 40, 20, 'Manisha', 100, 500, [700, 800], 250, 350]

#
listOne.remove(100)         # remove first occurence
print(listOne)

# listOne.remove([700, 800])         # remove first occurence of the list mentioned
listOne.remove(l3)           # remove first occurence of the list mentioned
print(listOne)

#
# listOne.remove(900)         # error if the value does not exist in the list
# print(listOne)
#
#
listOne.pop()           # it will remove the last element from the list (e.g. 350 here)
print(listOne)
#
listOne.pop(1)
print(listOne)