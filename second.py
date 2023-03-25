str ="resistance"
first =str.index('s')

second = str[first+1:].index('s') + first+1
print(first,second)