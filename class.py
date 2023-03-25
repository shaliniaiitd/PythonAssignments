"""sqr = lambda a : a**2
a=3

print(f"{a}:{sqr(a)}")
"""
class Employee:
    def __init__(self):
        self.id =1
        self.fName ='Shalini'
        self.mName =' '
        self.lName = 'Agarwal'
        self.aadharNo=1234785
        self.ppfNo =454676157
        self.salary =52389.855
        self.bank ='SBI'
        self.designation = 'Asst.Prof'
        
emp1 = Employee()
print(emp1.fName,emp1.salary,type(emp1))

class Student:
    def __init__(self):     # constructor   dunder init
        self.rollNo = 1
        self.name = "Sachin"
        self.contact = 55555
        self.city = "Mumbai"


# main script
# a = 5
# int a = 5;
stud1 = Student()
print(stud1.rollNo)
print(stud1.name)
print(stud1.city)
print(type(stud1))

stud2 = Student()
print(stud2.name)
print(type(stud2))
