import datetime    

"""a1. Print a fibonacci series (first 10 numbers from the series) using recursive function call
Fibonacci series is 0 1 1 2 3 5 8 13 ...
(it starts with 0 and 1, we keep getting the next number in the series by adding latest two numbers in the series)"""
def fib(n):
    list =[0]
    if n==1:
       return(list)
    list.append(1)
    if n==2:
        return (list)
    for k in range(2,n):
        list.append(fib(k)[-1]+fib(k-1)[-1])
    return(list)
 
print(fib(1))
print(fib(2))
print(fib(10))

#2. Write a lamda function to calculate cube of a number
cube = lambda x : x **3

x=7
print(f"{x } : {cube(x )}")
"""3. use (call) the sqr lambda function which we had created to print following number: square of that number for first 10 numbers.
	# 2: 4
	# 3: 9
	# 4: 16
	...
	# 10: 100
"""
sqr = lambda y : y**2
for j in range(1,11):
    print(f"{j}: {sqr(j)}")
    
"""4. Create a class for Employee with appropriate fields (or properties) and values. : DONE
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
"""

#5. Create a class for Employee with appropriate fields (or properties) and parmeterized values to create objects with different values.details:
"""Create a class for Employee with properties/ attributes: emp_no, first_name, last_name, dept, sal	
Make a provision to initialize the object being created
create 3 objects of type Employee
print first_name and sal of all 3 employees"""
class Employee:
    co_name ="ABC"
    count= 0
    def __init__(obj,  emp_no, first_name, last_name, dept, sal):
         obj.emp_no = emp_no
         obj.first_name= first_name
         obj. last_name = last_name
         obj.dept = dept
         obj.sal=sal
         Employee.count = Employee.count +1

#getters
    def get_emp_no(obj):
        return obj.emp_no
    def get_first_name(this):
        return this.first_name
    def get_last_name(a):
        return a.last_name
    def get_dept(self):
        return self.dept
    def get_sal(ref):
        #sal =10000
        return ref.sal
     #   return sal
#setters
    def set_emp_no(self,emp_no):
        self.emp_no =emp_no 
    def set_sal(self,sal):
        self.sal = sal
    def update_sal(obj,hike):
        obj.sal += hike*0.01*obj.sal
    def update_dept(this,dept):
        this.dept = dept
#decorator
    @classmethod
    def update_co(cls,name):
           cls.co_name =name
    @staticmethod
    def is_holiday(day):
         if (day.weekday ==6):
             return "True"
         else:
             return "False"
        
Employee.update_co("XYZ")
emp =[1,2,3]
print(Employee.co_name)
print(Employee.count)
#Employee.update_co("BCD")
emp[0]=Employee(1,"shalini","agarwal","physics",40000)
#print(help(datetime))
#today = datetime.today
emp[0].update_co("EFG")
print(Employee.count)
Employee.location ="Delhi"
print(Employee.location)
print(emp[0].location)
#print(help(Employee)) # prints all attributes of class Employee
emp[1]=Employee(2,"first","last","maths",60000)
print(Employee.count)
print(emp[1].co_name)
emp[2]=Employee(3,"radha","sinha","logistics",80000)
print(Employee.count)
#for e in emp:
 #   print(e.first_name , e.sal,type(e))
#6. Create a class for Employee with appropriate getters and setters methods.
emp[0].update_sal(50)
emp[0].update_dept("computers")
for e in emp:
    print(e.get_first_name(), e.get_sal(),e.get_dept(),type(e))

#A. Add a method to get salary of an employee. 
#B. Add a method to Employee class to increase the salary of employee by certain amount (pass hike as an argument).

#C. Add a method to modify the dept

"""7. Using this instead of self
A. define one of the above method (Employee class) by using a paramter name as this instead of self and use it.
"""
#8. Try to define a method inside Employee class to display full_name of the employee without using self or any similar parameter does it work?
# how to print all the attributes of a class
#print(Employee.__dict__)
#print(help(Employee))
#______assignment11________
"""On existing Employee class, from previous session, implement following scenario:
1. Make a provision for all employees to have a company name
  Access it using class name, as well as, objects, and check if you are able to access and print it or not.
  (Hint: create a class level property company_name)
  """
  
"""2. I want to track count of all employees and should be able to print the count at any given point of time.
  (Hint: create a class level property no_of_employees initialize to 0. increament it in __init()__ )
3. Create a class level method which can be called by any object, to modify the company name (Class Property)
  which should get reflected to all objects automatically. (Hint: use @classmethod decorator with cls param)
4. Write a generic method isWorkingDay() (Note: It should not be able to modify the class level properties)"""
print(emp[2].is_holiday(datetime.date.today()))