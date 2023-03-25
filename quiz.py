# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

#ValueError: attempt to assign sequence of size 6 to extended slice of size 5

a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a)

def f(i, values= []):
    values.append(i)
    print (values)
#    return values
f(1)
f(2)
f(3)

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
print(fruit_list1,fruit_list2,fruit_list3)
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    print(ls)
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print (sum)