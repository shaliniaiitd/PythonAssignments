n = int(input("Please enter a three digit number:"))

d1 = n//100; d23 = n%100
d2 = d23//10; d3 = d23%10
print("First digit of %d is %d, second digit is %d and third digit is %d" %(n,d1,d2,d3,))