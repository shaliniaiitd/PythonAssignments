

a = (8,)
print(type(a))

X=10,

print(type(X))

list1 = ['1','A','2','B']

list2 = [ int(el) **3 if el.isnumeric() else  el*3 for el in list1 ]

print(list2)

def func(list1,pow):
    list2 = [int(el) ** pow if el.isnumeric() else el * pow for el in list1]

    return list2

print(func(list1,4))


def rev(txt):
    r = txt[::-1]
    return r

txt = 'shalini'
print(rev(txt))

def c_palindrome(txt):
    if rev(txt) == txt :
        return True
    else:
        return False

print(c_palindrome(txt))



d = {"one": 1, "two": 2}

e = {"three": 3, "four": 4}

d.update(e)

print(d)

Z = {1:2, 1:4}

print(Z)

# [0,1,1,2,3,5,8,13,21]
# fib[n] = fib[n-1] + fib[n-2]
# fib_f(1) = [0]
# fib_f(2) = [0,1]

def fib_f(n):

    fib = [0]
    if n ==1:
        yield fib
    fib.append(1)

    if n == 2:
        yield fib
    else:
        for i in range (2,n+1):
            yield (fib[i-1] + fib[i-2])
            fib.append(fib[i-1] + fib[i-2])

        yield fib


print(fib_f(1))
print(fib_f(2))
print(fib_f(10))





















