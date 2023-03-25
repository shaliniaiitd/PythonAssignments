# colors = ['red', 'blue', 'orange', 'green', 'yellow']
# uppercase_colors = []
#
# for color in colors:
#     uppercase_colors.append(color.upper())
#
# print(uppercase_colors)     # ['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']

# colors = ['red', 'blue', 'orange', 'green', 'yellow']
# uppercase_colors = [color.upper() for color in colors]
# print(uppercase_colors)     # ['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']

# print(list(color.upper() for color in colors))  # print directly
# --------------------------------

# colors = ['red', 'blue', 'orange', 'green', 'yellow']
# warm_colors = []
# for color in colors:
#     if color in ['red', 'orange', 'yellow']:
#         warm_colors.append(color.upper())
# print(warm_colors) # ['RED', 'ORANGE', 'YELLOW']

colors = ['red', 'blue', 'orange', 'green', 'yellow']
warm_colors = [color.upper() for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors) # ['RED', 'ORANGE', 'YELLOW']