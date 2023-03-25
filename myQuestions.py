#Input = <p>end of report &#x20;</p>
#Output =******End Of Report*****

str = "<p>end of report &#x20;</p>"
print(str.strip('<>p,&#x20; / ').title().center(45,"*"))

#2 Take a multiline string. store each line in  separate variables.

txt = """ This is line 1
This is line 2
This is line 3
"""
b =txt.splitlines()
x,y,z = b
print(x,y,z)
#another way
c = txt.split('\n')
print (c[0], c[1],c[2])
