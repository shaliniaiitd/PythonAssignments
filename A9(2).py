`# 1) Write a `split_name` function that takes a string and returns a dictionary with first_name and last_name
def split_name(str):
    split =str.split(' ',1)
    d ={'first_name': split[0], 'last_name': split[1]}
    return d

repr(split_name("Shalini agarwal"))
assert split_name("Shalini Singh Agarwal") == { "first_name": "Shalini", "last_name": "Singh Agarwal",}, \
    f"Expected {{'first_name': 'Shalini' 'last_name': 'Singh Agarwal'}} but received {split_name('Shalini Singh Agarwal')}"
    #return d
#print(split_name('Kevin h Bacon'))

# 2) Ensure that `split_name` can handle multi-word last names

"""assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"
"""
# 3) Write an `is_palindrome` function to check if a string is a palindrome (reads the same from left-to-right and right-to-left)
def is_palindrome(a):
    a =repr(a)     #returns string representation of an evaluation.
    if a[: : -1] == a:
        return True
    else:
        return False

assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

# 4) Make `is_palindrome` work with
num =101
assert is_palindrome(num) == True, f"Expected True but got {is_palindrome(num)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

# 5) Write a `build_list` function that takes an item and a number to include in a list
def  build_list(string,num=1):
    list1 =[]
    for m in range(num):
        list1.append(string)
    return list1
        
assert build_list("Apple", 2) == [
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', ]' but received {(build_list('Apple', 2))}"
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"
