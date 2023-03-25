numbers = [918, 237, 1024,412, 567, 826, 237, 866, 950]
#numbers = [918, 236, 412, 566, 826, 238, 866, 950] 
#1. from the list of numbers, print only even numbers (hint: check for even number condition num % 2 == 0)
"""while (numbers):
    number = numbers.pop()

    if number%2 ==0:
        print(number, end=' ')
"""
#2. from the list of numbers, until you find an odd number (it should not navigate thru further numbers in the list)
"""while (numbers):
    number = numbers.pop()

    if number%2 ==1:
        print(number)
        break
else:
    print("\n no odd number")"""

#3. Try the first program of even numbers again, by making use of continue (hint: skip odd numbers)

i=-1
while i< len( numbers)-1:
    i = i + 1
    print(i)
    if numbers[i] %2==1:
        continue
    else:
        print(numbers[i])

#4. 
players = ['Sachin', 'Dhoni', 'Virat', 'Kapil', 'Sunil']
#print names of first 3 players only (hint: don't navigate thru' further names when you find "Virat")
for player in players[:3]:
    print(player)

"""5. for the same list of players 
   print names of first 3 players only 
   Hint: make use of slice
   for player in players[:3]:"""
#6. print the list of player names in reverse sequence (hint: use reversed() method)
print(players)
print(players[-1::-1])
players.reverse() # returns none.
print(players)


#7. print the list of players in sorted order of the names (hint: use sorted() method)
print(players)
print(sorted(players))
#8. for the program2, if there is no odd number found in the list, print a message "Only even numbers were available"
#9. find the maximum number from numbers list and print it using the else part of for loop
max =0
for num in numbers:
    if num>max:
        max = num
else:
    print("max=", max)

#10. find the sum of all numbers from numbers list and print it using the else part of for loop
sum=0
for num in numbers:
    sum +=num
else:
    print('sum=', sum)
    
#11. consider a list of salary. Increase the salary by 10% if salary is less than 50000 otherwise increase it by 5%
salaries =[10000,500,55000,3500,65000]
print(salaries)
newsal =[]
for sal in salaries:
    if sal < 50000:
        sal = 1.1*sal
    else:
        sal *= 1.05
    newsal.append(sal)
print(newsal)