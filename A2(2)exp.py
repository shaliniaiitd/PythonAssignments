n1= (input("please enter1st no.:"))
if type(n1) == 'str':
	print("Please enter an integer:")
n2=int(input("please enter2nd no.:"))
n3=int(input("please enter3rd no.:"))

if n1>=n2 and n1>=n3:
	ans =n1
elif n2>=n1 and n3 >=n2:
	ans = n3
else :
	ans = n2
	
print(f"max of {n1}, {n2} and {n3} is {ans}")