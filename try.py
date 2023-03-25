txt = 'shalini'
print(txt[::2])

a = (2),
b = int(),
print(type(a))      #Tuple
print(type(b))      #Tuple



eSet = {}
print(type(eSet))   # dictionary

eset = set()
print(type(eset))

s4 = {1, 2, 5, (22, 11, 33)}        # tuple is allowed
t = (1,2,3)
print(s4)
#s4.update((3,8))
s4.add(t)
print("after update", s4)

del (s4)

#s5 = {1, 2, 5, [22, 11, 33]}        #  TypeError: unhashable type: 'list'
#print(s5)

#s6 = {1, 2, 5, {22, 11, 33}}        #  TypeError: unhashable type: 'set'
#print(s6)