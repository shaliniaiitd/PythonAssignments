
# A valid email address has four parts:
#
# Recipient name
# @ symbol
# Domain name
# Top-level domain


err = "SORRY INVALID EMAIL"

#cHECK FOR @
str=input("please enter an email address:")
#1.
count = str.count('@')
# check for spaces
if str.count(" ") >0 or count == 0 or count >1:
    print('1',err)
    exit()

strP = str.partition("@")
#print(str)
username = strP[0]; sep = strP[1]; dName = strP[2]

#Check User name

# The recipient name may be a maximum of 64 characters long
if len(username) > 64 :
    print('2',err)
    exit()


# consist of:Uppercase and lowercase letters in English (A-Z, a-z)
# Digits from 0 to 9

spl = "! # $ % & ' * + - / = ? ^ _ ` { |"
splList = spl.split(" ")

#print(splList)
l = len(username)
i = 0
while i< l :
# print(username[i])
 if (username[i] not in splList) and username[i].isalnum() == False :
        print('3',err)
        exit()
 else:
        i = i+1

# Domain names may be a maximum of 253 characters and consist of:
if (len(dName) > 253):
    print('4',err)
    exit()
else:
    # allowed values: Uppercase and lowercase letters in English (A-Z, a-z)
    # Digits from 0 to 9
    # A hyphen (-)
    # A period (.)  (used to identify a sub-domain; for example,  email.domainsample)
    
    dSpl = ['-', '.']
    d = len(dName)
    i = 0
    while i< d:
 #        print(dName[i])
         if (dName[i] not in dSpl) and dName[i].isalnum() == False :
            print('4',err)
            exit()
         else:
            i = i+1
   
# Top-level domain
# Top-level domains are the highest level of the domain name system for the Internet and is placed after the domain name in an email address.
#
# Common top-level domains are:
# .com
# .net
# .org

#check for valid top domain name

topdnList = {'com','net','org','edu', 'in'}
if dName.split('.')[-1] not in topdnList:
    print('5', err)
    exit()
    
#A special character cannot appear as the first or last character in an email address
if str[0].isalnum() == False or str[-1].isalnum() == False :
#if str[0] in splList or str[-1] in splList:
      print('6', err)
      exit()
else:
   # spl characters cannot appear consecutively two or more times. 
    s = len(str)  ;  i = 0; consq =0
    splList.append('@')
    splList.append('.')
    while i < s :
      #  print(f"{str[i]}  : consq ={consq}")
        if   str[i] in splList and str[i-1] in splList:
           consq = consq + 1
     
        i = i +1
    
    if consq > 1:
        print('7', err)    
        exit()
    else:

        print("VALID EMAIL ID")
    #Test cases
# Email address
#
# What makes it invalid
#
# @domainsample.com
#
# The recipient name is missing.
#
# johndoedomainsample.com
#
# The @ symbol is missing between johndoe and domainsample.com.
#
# john.doe@.net
#
# The domain name (domainsample) is missing after the @ symbol and before the top level domain (.net).
#
# john.doe43@domainsample
#
# The top level domain (.co.uk) is missing.