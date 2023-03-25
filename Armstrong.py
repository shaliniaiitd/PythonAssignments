# T = int(input("no. of cases:"))
#
# while (T):
#     T = T-1
#     num= input("Number:")
for num in range(1000):
    power= len(str(num))
    divisor = 10 ** power
    sum = 0
    n = int(num)
    while(n):
        d = n//divisor
        n = n%divisor
        divisor = divisor/10
        sum = sum + d**power

    if sum == int(num):
        print(num , "is ARMSTRONG")


