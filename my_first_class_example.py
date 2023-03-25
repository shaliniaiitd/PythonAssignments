#1. Create module - my_first_class_example.py
#2. Create a Circle class
class Circle :
    no_of_circles  =0
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
  # instance variables - radius, color
    def set_radius(self,radius):
        self.radius=radius
   #area() - formula is 3.14*raidus**2
    def area(self):
           return(3.14*self.radius**2)
           
      #perimeter() - 2*3.14*radius
    def perimeter(self):
            return(2*3.14*self.radius)           
"""3.. Create two circle object references c1 and c2 pointing to Circle objects. c1 with radius = 9, color - "White"
	 c2 with radius = 11, color - "Yellow"
	print the area and perimete of c1 and c2"""
c1 = Circle(9,"white")
c2 = Circle(11,"yellow")
a  =c1.perimeter()
print(f"area of c1= {c1.area()}, perineter = {c1.perimeter()}")

print(f"area of C2 ={c2.area()}, perimeter={c2.perimeter()}")
	
"""4. Change the radius of c1 from 9 to 15 and change the radius of c2 from 11 to 3"""
c1.set_radius(15)
c2.set_radius(3)

print(c1.radius, c2.radius)
"""5. Print area and perimeter of c1 and c2 and verify that it reflects the changed value"""
print(f"area of c1= {c1.area()}, perineter = {c1.perimeter()}")

print(f"area of C2 ={c2.area()}, perimeter={c2.perimeter()}")
	