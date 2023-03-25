from collections import deque


"""1)	Write a Python program to reverse any number:
    Input : 1234
    Output: 4321 
"""

num= str(1234)
print(num[: :-1])


"""2)	Write a Python program to find the number of 'E' in the string SELENIUM?
    Input : SELEN))IUM 
    Output: No. of Es in the string supplied are 2
"""
st ="SELENIUM"
print(st.count('E'))
    
#3)	Write a program  
inp = [4,5,6,-8,0,-6,7,-3,0,9,-5]
num =0
while 0 in inp:
    inp.remove(0)
    num += 1  
 
#d=deque(inp)
j =0
while j< num : 
   # d.appendleft(0)
   inp.insert(0,0)
   j+=1

print(inp)

   # Output: {0,0,4,5,6,-8,-6,7,-3,9,-5}
    

"""4)	Print all the numbers  from 1 to 50 but   
        
    Output : when the number  divisible by 3 print abc, 
             divisible by 5 print def, 
             divisible by 10 print abcdef."""
j=0
for j in range(1,51):
       if j % 10==0 : 
           print('ghi')
       elif j % 5 ==0:
           print('def') 
       elif j % 3==0:
            print('abc')
       else:
            print(j,end =':')   
             
#5)	Write a program to print a pattern of stars in triangle shape?
n =4
m =0
for m in range(1,n):
        print('*' * m)
    
#6)	Write a program to find out first 10 prime numbers ?
prime =[]
for j in range (1,100):
    if len(prime) ==10:
        break
    d =0
    for k in range(2,j):
        if j%k ==0:
                d =1
                break
    if d ==0:
        prime.append(j)
        
print(prime)

#7)	Write  a program to find a given number is even or odd without using modulus operator?
num=75
if (num//2)*2 == num:
    print(num, "is even")
else:
    print(num, "is odd")

#8)  Write a Python program to swap two numberswithout creating a temporary variable.
a=10
b=20
a,b=b,a
print(a,b)

"""9) Fibonacci series Write a Python program to print fibonacci series
without using recursion and using recursion.
Input: 10
Output: 0 1 1 2 3 5 8 13 21 34"""
n =10
fib =[0]
fib.append(1)

for j in range(2,10):
        fib.append(fib[j-1] + fib[j-2])
print(fib)

#using recursion
def fibnocci (n):
    fib =[0]
    if n ==1:
        return(fib)
    fib.append(1)
    if n==2:
       
        return(fib)
    else:
        for j in range(2,n):
            fib.append(fibnocci(j-1)[-1] + fibnocci(j-2)[-1])
    return (fib)

print(fibnocci(10 ))


"""10) Prime number

Write a Python program to check prime number.

Input: 44

Output: not a prime number

Input: 7

Output: prime number

11) Palindrome number

Write a Python program to check palindrome number.

Input: 329

Output: not palindrome number

Input: 12321

Output: palindrome number

12) Factorial number

Write a Python program to print factorial of a number.

Input: 5

Output: 120

Input: 6

Output: 720

13) Armstrong number

Write a Python program to check Armstrong number.

Input: 153

Output: Armstrong number

Input: 22

Output: not Armstrong number

14) Bubble Sort

Write a Python program to sort an array elements using bubble sort algorithm.

Input : 50 20 6 103 67 2 9

Output: 2 6 9 20 50 67 103

15) Selection Sort

Write a Python program to sort an array elements using selection sort algorithm.

Input: 16,37,4,45,9,78,92

Output: 4,9,16,37,45,78,92	

16) Insertion Sort

Write a Python program to sort an array elements using insertion sort algorithm.

Input: 15 6 30 2 50 28

Output: 2 6 15 28 30 50

17) Input String given is "I love my Company"
You need to change this to show outputs as below
Input: I love my Company
Output a: ynapmoC ym evol I
Output b: I LovE MY CompanY

18) Find duplicate characters in a given string.
Input: internationalization
Output: i-4,n-4,t-3,a-3,o-2

19) Write a program to obtain the output based on input given below.

Input:"aaabbcddd"

output: a3b2c1d3
"""


