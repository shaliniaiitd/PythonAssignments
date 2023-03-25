age = int(input("Please enter your age: ")) 
 """ the value received using input() method is always String
 fjdfjfkfkgk
# use int() to convert it into integer format"""
print(type(age))

if age <= 18:
    status = "kid"
elif age < 60:
    status = "working"
elif age >= 80:
	status = "awesome!"
else:
    status = "retired"

print("You are ", status)