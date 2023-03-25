"""2. Write a menu driven program
	** MENU **
	1. Add
	2. Sub
	3. Mul
	4. Div
	5. Mod
	6. Quit
Ask for the user's choice and based on that display the result till user enters 6
Display menu"""

print("Menu".title().center(10,'*'))
options =dict(add=1,sub=2,mul=3,div=4,mod=5,quit=6)
for key in options.keys():
    print(f" {options[key]}. {key}")
    
option=0
while option !=6:
    option = int(input('please choose an option number'))
    print(2+3)  if  option ==1  else print(2-3) if option==2  else  print(2*3)   if option ==3  else print(2/3) if option ==4  else  print(2%3) if option ==5 else print('goodbye') if option ==6 else print('please enter a number between 1 and 5')
    
#4. Understand the following prprintgram by executing it

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# # Verify each user until there are no more unconfirmed users.
# #  Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user.title())
# # Display all confirmed users.
print("\nThe following users have been confirmed:")
#for confirmed_user in confirmed_users:
#while(confirmed_users):
    # print(confirmed_users.pop().title()) 
print(confirmed_users)

#5. In a list (you can refer the same list which we had used in example "numbers". 
#check if number 237 is available or not. If avaialble print the number, otherwise print "number not found".
#Implement using while loop.
#numbers = [918, 237, 412, 566, 826, 237, 866, 950]

numbers = [918, 236, 412, 566, 826, 238, 866, 950] 

i =0
while 237 in numbers: 
        i = i+1
        print(i)
        print(237)
        break 
else:
        print('number not found')

#6. 
#7. 
listOne = [1, 2, 3, 50, 60]
#create another list with name square_list using list comprehension to include squares of these numbers
#(do it only for the numbers which are less than 4)
square_list = [val**2 for val in listOne if val <4]
print(square_list)

#8.
listOne = [1, 2, 3, 50, 60]
#create a dictionary using dictionary comprehension to include key: squares of key
d = {key : key**2 for key in listOne}
print(d)
#9. create a dictionary using dictionary comprehension to include key: squares of key
#(do it only for the numbers which are less than 4)
print(dict({key : key**2 for key in listOne if key <4}))

#10
empData = {'1a': 'abc', '2a': 'xyz'}
print(dict({key : empData[key].upper() for key in empData.keys()}))
# # exp output: {'1a': 'ABC', '2a': 'XYZ'}

#11
employees = {'Sachin': 5000, 'Dhoni': 6000, 'Virat': 7000, 'Kapil': 8000, 'Sunil': 9000}
print(employees)

#create a new dictionary and include the values: increase salary of each playter by 10%, 
dNew = {key: employees[key]*1.1 for key in employees.keys()}
print(dNew)
#12.
#create a new dictionary and include the values: increase salary of each playter by 10%, only if the salary is <8000
dNew = {key: employees[key]*1.1 for key in employees.keys() if employees[key] < 8000}
print(dNew)

#13. Try following examples for range:
print(list(range(1, 5)))   
print(list(range(1, 10)))   
print(list(range(1, 10, 2)))
print(list(range(0, 10, 2)))

#14.  print 3, 4, 5 by using for loop with range
for num in range(3,6):
    print(num)
        
#15  print 3, 5, 7 by using for loop with range
for num in range(3,8,2):
    print(num)

#16. 
players = ['Sachin', 'Dhoni', 'Virat', 'Kapil', 'Sunil']
#Print index and player name. 
for j in  range(len( players)):
    print(j, players[j])

#(hint: use range() and len() in for loop)
