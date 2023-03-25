#Get a string from user and count #number of occurrence of each letter within that

str = input("enter a string:")

for val in set(str):
	count =str.count(val)
	print(f'{val} = {count} times')
