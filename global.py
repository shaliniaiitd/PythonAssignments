#We also talked about the global keyword which lets you modify the value of a global variable

#global y
y= 10
def mod_x():
	global y
	y = y+2
print(y) # x = 12

#or make a local variable accessible outside its scope.

def func():
	global x
	x = 10
print(x)  # prints 10
