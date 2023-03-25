# Explanation of list related functions list1.sort() vs sorted(list1)
# list1 = [10, 50, 20, 30, 80]
# # list1.sort()      # contents of list1 will be sorted  but it won't return anything
# # print(list1)    # [10, 20, 30, 50, 80]        # contents of list1 will be sorted but it won't return anything
#
# # print(list1.sort())     # None
# # list2 = list1.sort()    # list2 will contain  None
# # print(list2)            # None
#
# # contents of list1 will not be sorted but we can print or store the contents in sorted order
# print(sorted(list1))       # contents of list1 will not be sorted but we can print the contents in sorted order
# # list2 = sorted(list1)   # list2 will contain  sorted numbers,
# # print(list2)            # sorted numbers
# # print(list1)            # original contents of list1