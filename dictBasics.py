# hash or 'associative array' or map or dictionary

# key, value pairs
# key and value is separated using colon(:)
# key, value pairs are separated using comma(,)
# keys can include Immutable types (so no lists are allowed as key)
# key has to be unique (no duplicates are allowed)
# but values can be duplicate
# we create dictionary using curly braces {}
# dictionaries are ordered (as per the insertion order): python 3.7 onwards
# (Python2: by default unordered, OrderedDict)
# each key value pair is an item

# ages = {'Kevin': 59, 'alex': 29, 'bob': 40}
# print(ages)     # {'Kevin': 59, 'alex': 29, 'bob': 40}
#
# print(ages['Kevin'])       # 59
# # print(ages['Ravi'])       # KeyError: 'Ravi'
#
# ages['prerna'] = 21
# print(ages)
#
# ages['Samita'] = 21
# print(ages)
#
# ages['prerna'] = 19
# print(ages)
#
# ages['bob'] = 22
# print(ages)
#
# del ages['alex']
# print(ages)
#
# # del ages
# # print(ages)        # ages not accessible after deleting it
# #
# # ages.clear()
# # print(ages)
# #
# # print('Manisha' in ages)    # False when dictionary is empty
# # print('Samita' in ages)    # True without clearing dictionary
# # print('Karan' in ages)    # False
# # print('Bhanesh' not in ages)    # True
#
# # ages.pop()  # error
# # ages.pop('kevin')   # keyError as key is case sensitive
# print(ages.pop('Kevin'))  # it will remove the key value pair and return the value e.g. 59
# print(ages)
#
# print(ages.popitem())   # it will remove and return the last item (key, value pair)
# print(ages.items())
#
# print(ages.keys())
# print(ages.values())
#
# print(type(ages))

# ================================
# Another way to define a dictionary using dict() with Keyword Arguments
wts = dict(kevin=60, bob=40, kayla=90)
print(wts)      # {'kevin': 60, 'bob': 40, 'kayla': 90}

# Another way to define a dictionary using dict() with a list of tuples
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
print(colors)

colors = {}
print(colors)