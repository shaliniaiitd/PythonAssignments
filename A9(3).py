# 1. Create a method which accepts
# name, middle name and surname as parameters
# and returns the full name.
# but make middlename as optional

def name(fname,lname,mname=' '):
    return(fname.title()+ ' ' + mname.title()+ ' '+lname.title())
    
print (name('shalini','Agarwal'))
print(name('pardeep','Jamwal','singh'))

#2. In the above method, modify such that it returns the dictionary with the following format
# {'name': 'Simon', 'surname': 'Stuart' }
def name(fname,lname,mname=' '):
    return(dict(name=fname, surname=lname))
    
print(name('shalini', 'agarwal'))

# 3. Call the above method in a while loop which accepts name and surname from user
#    and prints the dictionary.
#    if user gives 'q' as the input for either name or surname then exit the loop
"""ans =input('at any stage,press q to quit and  y to continue')
if ans == 'q':
    break   
while (ans != 'q'):
   print()
   # fname = input('enter '
   else:
        break
    """



# 4. Write a function which will accept the variable number of parameters
#    This is toppings one needs in a pizza
#    Print the toppings on console
def  pizza(*toppings):
    while topping in toppings:
        
    print(toppings)
    
pizza('chrese','capsicum', 'tomato', 'onion',('mushroom','babycorn'))

