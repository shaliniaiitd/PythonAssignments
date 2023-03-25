set1 = {1,2,3,4,5,6}
set2={3,4,5}
print(set2 <= set1)
print(set2.issubset(set1))
    
# print 3, 4, 5
for i in range(3, 6):      # 3,4,5
   print(i)

# # print 3, 5, 7
for i in range(3, 8, 2):
    print(i)

# # create a list for squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print( squares)

# # How else range can be useful
# # I want to print index and player name. Though it may not be frequently required.
players = ['Sachin', 'Dhoni', 'Virat', 'Kapil', 'Sunil']
for i in range(len(players)):
   print(i, players[i])
