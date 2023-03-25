s1 = input("enter the first string.py:")
s2 = input("enter the second string.py:")
if s1 == s2:
    print("strings are same")
else:
    print("strings are not same")

s = s1 + s2

print("Concat", s, sep="$")
print(f"Concat {s1} and {s2} is {s}")

# another way of printing
print(" answer %s + %s = %s" % (s1, s2, s), s, sep="$", end="****************************")