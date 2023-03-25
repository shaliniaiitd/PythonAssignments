 #rec1 = "Sachin,Tendulkar,Mumbai,India,45565,Cricket"
# assignment: implement it using split, similar to url
# hint: , is a separator

rec1 = "Sachin,Tendulkar,Mumbai,India,45565,Cricket"

print(rec1.split(','))

rec2 =rec1.replace(',', '\t')
print(rec2)
print(rec2.split('\t'))

