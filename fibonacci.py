def fib_f(n):
    fib = [0]
    if n == 1:
        return (fib)
    fib.append(1)
    if n == 2:

        return (fib)
    else:
        for j in range(3, n+1):
            fib.append(fib_f(j - 1)[-1] + fib_f(j - 2)[-1])
    return (fib)


# print(fib_f(5))


# def fib_f(n):
#     if n<2:
#         return n
#     else:
#         return fib_f(n-1) + fib_f(n-2)

print(fib_f(5))

