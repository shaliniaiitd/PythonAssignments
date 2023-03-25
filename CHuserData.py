#Print data of 5 users in a tabular format
#Consider fields:
#UserId FirstName LastName City #Mobile Income

num= int(input("Please enter number of users"))
sep = input("Please enter data separator")
fields =int(input("no. of fields"))

dataList=list(); i=0

while i<num :
	print(i)
	dataList.append(input(f"Please enter data for user {i}"))
	i=i+1

format =[10,10,10,10,12,10]
headers = ["UserId", "FirstName", "LastName","City","Mobile","Income"]

print(type(headers))
#covert tuple into string
header =("").join(headers)
print(header)

#print headers
result = list()

j=0	
while j<fields :
	print("j =", j)
	result.append(headers[j].ljust(format[j]))
	j =j +1
print(result)
	
#print user data
printList  = list()

for user in dataList:
	f =0
	while f<fields:
			#print("f=", f)
			userData = user.split(sep)
			printList.append(userData[f].ljust(format[f]))
			f =f + 1
			
print(printList)