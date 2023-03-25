# # range(start, stop, step)      # start is inclusive, stop is not inclusive, by default step is 1
#
# my_range = range(10)
# print(my_range)     # range(0, 10)   values to iterate 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#
# # for i in my_range:
# #     print(i)
#
# print(my_range[0:5])    # range(0, 5)
# print(my_range[5:0:-1])    # range(0, 5)
#
# # for i in my_range[0:5]:
# #     print(i, end=" ")              # 0, 1, 2, 3, 4
# #
# for i in my_range[5:0:-1]:
#     print(i, end=" ")              # 0, 1, 2, 3, 4

# print(range(1,11))
# for i in range(1,5):
#     print("looping")

for _ in range(1,5):
    print("looping")

for i in range(5):      # 0 to 4
    print(i)

# print 3, 4, 5
# for i in range(3, 6):      # 3,4,5
#     print(i)

# # print 3, 5, 7
# for i in range(3, 8, 2):
#     print(i)
#
# # create a list for squares
# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
#
# print(squares)

# # How else range can be useful
# # I want to print index and player name. Though it may not be frequently required.
# players = ['Sachin', 'Dhoni', 'Virat', 'Kapil', 'Sunil']
# for i in range(len(players)):
#     print(i, players[i])
#