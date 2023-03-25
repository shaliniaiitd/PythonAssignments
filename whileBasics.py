# while CONDITION:
#     pass

# while True:     # infinite loop
#     print("Looping")

# count = 1
# while count <= 5:
#     print("iteration", count)
#     count += 1

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# remove all instances of 'cat' from the list
# while 'cat' in pets:
#     pets.remove('cat')
# else:
#     print(pets)
#
while 'cat' in pets:
    pets.remove('cat')
print(pets)