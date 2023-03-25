# Passing List as a parameter
def greet_users(names,*num):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
    print(num)
# main script
usernames = ['sunil', 'nitin', 'karan', 'ravi']
t =(1,2,3,"anil")
greet_users(usernames,t,7,8)