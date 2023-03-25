"""1. print below triangle. (hint: using a for loop, range function, and * (mutiply) to repeat a string)
*
* *
* * *"""
for j in range(1,4):
    print(j*'*')
"""#2. print below pattern (hint: using nested for loops and range function)
* * *
* * *
* * *"""
for k in range(1,4):
        print(end='\n')
        for j in range(1,4):
            print('*',end=' ')
"""3. print below triangle (hint: using nested for loops and range function)
*
* *
* * *"""
for j in range(2,5):
    print()
    for k in range(1,j):
        print('*', end=' ')

"""4. print below triangle (hint: using nested for loops and range function)
* * *
* *
*"""
print()
for j in range(3,0,-1):
    print()
    for k in range(j,0,-1):
        print('*', end=' ')
"""
5. print below triangle (hint: using 2 nested for loops and range function)
* * *  (1 inner loop to print spaces,       another inner loop to print *)
  * *
    *	"""
print();s=0
for j in range(3,0,-1):
    s =3-j
    print()
    print(s*' ',end='')
    for k in range(j,0,-1):
        print('*', end='')


"""6. Write a program to check and print if a number is a prime number or not
Hint: a number is a prime number if it is not divisible by any number other than 1 and itself"""
num = input("input a number")
"""divisors =[]
for j in range(2,num):
    if num%j ==0:
        divisors.append(j)
print(divisors)
if len(divisors) ==0:
    print("number is prime")
else:
    print('number is not prime')
"""
#7. Write a function to Count the number of digits in a number (hint: using mod logic for the number) 
#
#print(len(num))
num = int(num)
q = num; j=0;sum=0
while(q>=1):
   # q = q//10
   q,r =divmod(q,10)
   sum +=r
   j+=1
print(j)
print(sum)

#8. Write a function to find the sum of digits in a number (hint: using mod logic for the number) 

#9. print the reverse of a a number 
num=str(num)

print('after reversal', num[::-1])

"""10. Print factorial of a number
factorial of number n is print * n-1 * ... * 1
e.g. factorial of 4 is : 4 * 3 * 2 * 1 which is 24
Note: Write a function to find and return factorial of a number
In the program, call the function print(fact(4))
Implement using 2 logics:
# logic 1
# 1 * 2 * 3 * 4

# logic 2
# 4 * 3 * 2 * 1"""

def fact(num):
        if (num<=1):
            return(1)
        
        return(num*fact(num-1))

def fact1(n):
      fact =1
      for t in range(2,n+1):
             fact=fact*t
      return(fact)
        
print (fact1(4))
"""11. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age .
#    If a person is under the age of 3, the ticket is free; if they are between 3 and 12,
#    the ticket is $10; and if they are over age 12, the ticket is $15 .
#    Write a loop in which you ask users their age, and then tell them the cost of their movie ticket .
After each iteration (after processing each user), ask a question "Do you want to continue (y/n)". 
Depending on the choice, continue the process or exit out of the loop."""

while ("True"):
    age = int(input("enter your age"))
    if age <3:
        fare =0
    elif 3<=age<=12:
        fare =10
    else:
        fare =15
    print("fare=", fare)
    ans =input("do you wish to continue Y/N")
    if ans.upper()== 'N':
        break

"""12. print a fibonacci series (first 10 numbers from the series, make use of while loop to count)
Fibonacci series is 0 1 1 2 3 5 8 13 ...
(it starts with 0 and 1, we keep getting the next number in the series by adding latest two numbers in the series),"""
a=0; b=1;temp=0,; l=0
print(a,b,end=" ")
while l in range(8):
    print(a+b,end=" ")
    temp = a+b
    a =b
    b = temp
    l+=1
    
#13
a,b,m=0,1, 0
print('\n', a,b, end=" ")
while m in range(8):
    print(a+b,end=" ")
    a,b = b, a+b    #using packing/unpacked ng
    m += 1

"""#13. print a fibonacci series (first 10 numbers from the series, make use of for loop with range function to count)
Fibonacci series is 0 1 1 2 3 5 8 13 ... 
(it starts with 0 and 1, we keep getting the next number in the series by adding latest two numbers in the series)
This time use of tuple packing, unpacking feature: 
a, b = 0, 1
a, b = b, a + b
"""