# Write a function that, when passed a list and a target sum, returns, efficiently with respect to time used, two distinct zero-based indices of any two of the numbers, whose sum is equal to the target sum. If there are no two numbers, the function should return None.
#
# For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the following pairs of indices:
#
# 0 and 3 (or 3 and 0) as 3 + 7 = 10
# 1 and 5 (or 5 and 1) as 1 + 9 = 10
# 2 and 4 (or 4 and 2) as 5 + 5 = 10

def func(list,target):
    result = []
    for i in range(0,len(list)):
        for j in range(i+1, len(list)):
            if (list[i]+list[j] == target):
                result.append((i,j))
            j= j+1
        i = i+1
    if len(result) !=0 :
        return result
    else:
        return ()

print(func([3,1,5,7,5,9],10))

#AFCTORIAL
def fact (n):
    if (n <2):
        return(1)
    else:
        return(n*fact(n-1))

print(fact(5))

# Implement the unique_names method. When passed two lists of names, it will return a list containing the names that appear in either or both lists. The returned list should have no duplicates.
#
# For example, calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']) should return a list containing Ava, Emma, Olivia, and Sophia in any order.

def merge(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    print(set(set1.union(set2)))
    print(set(set1|set2))

merge(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])


# Implement a group_by_owners function that:
#
# Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.
# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
# the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
dict1 = dict()
def group_by_owners(dict1):
    result = dict()

    for value in dict1.values():
        filename = list()

        for key in dict1.keys():
            if dict1[key] == value:
                filename.append(key)
        result.update({value: filename})
    return result

print(group_by_owners({'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}))

#Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with respect to time used, counts the number of list elements that are less than the parameter less_than.

#For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less than 4.

def count_numbers(sorted_list, less_than):
    print (less_than)
    number = 0
    i = 0
    while (sorted_list[i] < less_than):
        number += 1
        print("1:",number)
        i +=1
    print(number)
    return number


sorted_list = [1, 3, 5, 7]
print(count_numbers(sorted_list, 6)) # should print 2


def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """

    result = []
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j] == target_sum):
                result.append((i, j))
            j = j + 1
        i = i + 1
        # if len(result) !=0 :
    return result

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))

import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])



def contains(root, value):
        while (root):
            if value == root.value:
                return "True"
            elif value < root.value:
                root = root.left
            else:
                root = root.right

        return "False"

n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))

import collections


class TrainComposition:

    def __init__(self):
        self.wagonId = wagonId
        self.left = None
        self.right = None

    def attach_wagon_from_left(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the left
        """
        while (self.left):
            self = self.left

        self.left = wagonId

    def attach_wagon_from_right(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the right
        """
        pass

    def detach_wagon_from_left(self):
        """
        :returns: (int) The number of the wagon detached from left
        """
        pass

    def detach_wagon_from_right(self):
        """
        :returns: (int) The number of the wagon detached from right
        """
        pass


if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right())  # should print 7
    print(train.detach_wagon_from_left())  # should print 13


import math

