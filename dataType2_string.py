# Example for String data
s = '012345'  # string s defined with value 012345 assigned to it
print("Original string s = ", s)  # 012345
print("0th index charater from string s = ", s[0])  # 0
print("Character at -ve index -1 = ", s[-1])  # 5
# [start:end]       start is inclusive      end is not
print("String from 1 to 4 index = ", s[1:4])  # 123
print("String after index 2 =", s[2:])  # 2345
print("String upto 4 index = ", s[:4])  # 0123
print("-----------------------------------------------------")

str1 = "Consistent"
print("Original string str1  = ", str1)  # Consistent
size = len(str1)
print("length of str1 = ", size)  # 10
print("length of str1 = ", len(str1))  # 10
print("-----------------------------------------------------")

str = "Welcome to Python. Learn Python with Sunil"
print("Original string str  = ", str)  # Welcome to Python. Learn Python with Sunil
count1 = str.count('Python', 0, len(str))
# count1 = str.count('Python', 12, len(str)) # 1
print('Count of Python in str = ', count1)  # 2
print("-----------------------------------------------------")
print("String formats in Python = ")
print("one, %d, two" % 2)  # one, 2, two
print("%s two %s" % (1, 'three'))  # 1 two three
print("Hello repeated 3 times using * operator = ", 'Hello' * 3)  # HelloHelloHello
print("Checking existence of substring e in hello = ", 'e' in "hello")  # True
print("String from -2 to -5 index = ", 'hello'[-2:-5])  # empty Why? direction
print("String from 4 to 1 index = ", 'hello'[4:1])  # empty Why? direction
print("String from 4 to 1 index (with -1)= ", 'hello'[4:1:-1])  # oll
print("String from -2 to -5 index (with -1)= ", 'hello'[-2:-5:-1])  # lle
print("String from -3 to -1 index = ", 'hello'[-3:-1])  # ll
print("-----------------------------------------------------")