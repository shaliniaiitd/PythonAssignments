#1. consider a list
list1 = [10,60,130,40,[1,2,3]]

# A. Assign it to list2
# B. check if the values of list1 and list2 are same or not.
# C. print the id of element with value 60 and compare if its id in list1 and list2 is same or not
# D. compare the values of inner list and also compare the id of inner list for both list1 and list2. Check if it's same or different.

list2 = list1   #Shallow copy

assert(list1==list2)
print(id(list1[1]), id(list2[1]))       #2751345395792 2751345395792




# 2. consider a list
# list1 = [10,60,130,40,[1,2,3]]
#
# A. If I copy it to list2 using list1.copy method, is it an example of shallow copy or deep copy?
# B. copy it to list2 using copy method of copy module. Is it example of shallow copy or deep copy?
# C. check if the values of list1 and list2 are same or not.
# D. print the id of element with value 60 and compare if its id in list1 and list2 is same or not
# E. compare the values of inner list and also compare the id of inner list for both list1 and list2. Check if it's same or different.
#
#
# 3. consider a list
# list1 = [10,60,130,40,[1,2,3]]
#
# A. To copy the list1 contents to list2 recursively. Which method should be used over here?
# B. Use the appropriate method to copy the contents recursively to list2
# C. check if the values of list1 and list2 are same or not.
# D. print the id of element with value 60 and compare if its id in list1 and list2 is same or not
# E. compare the values of inner list and also compare the id of inner list for both list1 and list2. Check if it's same or different.
#
#
# 4. I have a list which I don't want to use further and ensure that no one is accessing it and doing some operations accidentally.
# Which option you would suggest to achieve this?
#
# 5. What would be output of following program
l1 = ["Sachin", "Rahul", "Virat", "Saurav", "Dhoni"]
l2 = ["Kapil", "Sunil", "Kirmani"]

#l2 += l1       #['Kapil', 'Sunil', 'Kirmani', 'Sachin', 'Rahul', 'Virat', 'Saurav', 'Dhoni']
l2.append(l1)   # ['Kapil', 'Sunil', 'Kirmani', ['Sachin', 'Rahul', 'Virat', 'Saurav', 'Dhoni']]
print(l2)
#
# Will it add l2 as an innerlist or it will add individual elements of l2 to l1?
#
# 5. Consider below code:
l1 = [10, 20, 30]
t1 = (100, 400, l1, 200, 300)
#
# Under t1, can I modify value 20 to 50? If yes, how? If no why?
# Yes, because list is mutable, lets check

t1[2][2] = 40
print(t1)           #(100, 400, [10, 20, 40], 200, 300)

# 6. Consider below code:
# t0 = (10, 20, 30)
# t1 = (100, 400, t0, 200, 300)
#
# Under t1, can I modify value 20 to 50? If yes, how? If no why?
# No, because tuples are immutable
#
# 7. Consider below code:
# t0 = (10, 20, 30)
# l1 = [100, 400, t0, 200, 300]
#
# Under l1, can I modify value 20 to 50? If yes, how? If no why?
# No, lets check
l1[2][1] = 1
print(l1)   #TypeError: 'int' object does not support item assignment
# 8. Consider below code:
# l0 = [10, 20, 30]
# l1 = [100, 400, l1, 200, 300]
#
# Under l1, can I modify value 20 to 50? If yes, how? If no why?
#
# YES
