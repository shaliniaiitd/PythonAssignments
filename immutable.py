# a = 10
# print("a = ", a, "id of a ", id(a))
#
# b = 10
# print("b = ", b, "id of b ", id(b))
#
# c = int(input("c "))    # 10
# d = int(input("d "))    # 10
# print("c = ", c, "id of c ", id(c))
# print("d = ", d, "id of d ", id(d))
#
# e = 5
# e += 5   # e = e + 5
# # d += 5
# print("e = ", e, "id of e ", id(e))
# print(a is b)     # True
# print(a is b is c)     # True
# print(a is b is c is d)     # True if d+=5 is not done. False if d+=5 is done

str1 = "Sunil"
str2 = "Sunil"
str3 = input("str3 ")  # Sunil  - gets different object/location in memory
str4 = input("str4 ")  # Sunil  - gets different object/location in memory
print('1', str1, id(str1))
print('2', str2, id(str1))
print('3', str3, id(str3))
print('4', str4, id(str4))
print('5', str1 is str2)  # pointing to same object?  True
print('6', str1 == str2)  # values same?  True
print('7', str3 is str4)  # pointing to same object?  False
print('8', str3 == str4)  # values same? True
 # str3[0] = "s"  # Runtime - TypeError: 'str' object does not support item assignment
# str1[0] = "s"  # CompileTime - Class 'str' does not define '__setitem__', [] cannot be used


str3 += " Gawaskar"
str4 += " Gawaskar"
print('9', str3 is str4)     # False
print('10', str3 == str4)     # True

str3 = " Gawaskar"
str4 = " Gawaskar"
print('11', str3 is str4)     # True
print('12', str3 == str4)     # True

str = "Arpit"
print("str =", str)

str.casefold()
print("casefold", str.casefold())

str1 = input("Please enter some text: ").casefold()     # useful for case insensitive search

print("str1 =", str1)
ch1 = input("Please enter the character to check how many times it exists in text " + str1 + ": ").casefold()

if str1.count(ch1) > 0:
    print(str1.count(ch1))
else:
	 print("Entered character does not exist in the text", str1)

url = 'https://example.com/users/jimmy'
user = url.split('/')[-1]
print(user)	 # 'jimmy'
user = url.split('/')
print(user)
print(user[-1])	 # 'jimmy'
print(user)	 # 'jimmy'