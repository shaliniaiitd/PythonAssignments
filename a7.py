#1. can we have different data types in set?

#2. For a tuple with the name b, print -b
b = (1,20)
print(-b)           #TypeError: bad operand type for unary -: 'tuple'

#3. try following add values of tuple  to set (update method)

#4. try following
#print(ages.item())
#5. for a dict with the name ages, implement following using for loop:
# print("All Values")
ages= dict([('a',1),('b',2),('c',3)])
print(ages)
for age in ages:
    print(ages[age])

#6. for a dict with the name ages, implement following using for loop:
# print("All Items")

for item in ages.items():
    print(item)


#7. During the session we had seen that we can create a new dict using dict() method by pssing a list of tuples to it
#On similar lines try to create a new dict passsing tuple of tuples. Check if it works or not.
d2 = dict(((1,2),(2,4),(3,8),(4,16)))
print("DICT created using tuple of tuples:", d2)

#Solve futher programs considering below list and for loop (Do not use ready methods available on list).
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,743, 527,237]
print(numbers)

#8. print the list using for loop. After printing the complete list, print "list printing completed" message.
#(hint: you may use else: here)
for number in numbers:
    print(number)
print("list printing completed")

#9. search a number 237 in the list and print if it is found or not.
#(hint: you may also use break here)
for number in set(numbers):
    if number == 237:
        print("Found 237 in list")
    break
#10. print all the numbers from the list, other than 237.
#(hint: you may try to use continue here)
for number in set(numbers):
    if number == 237:
        continue
    else:
        print(number)
#11. search a number 237 in the list and print how many times it appeared.
count =0
for number in numbers:
    if number ==237:
        count += 1
print(count)
#print(numbers.count(237))