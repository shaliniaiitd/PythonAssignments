class Student:  # PascalCase
    def __init__(self, roll, name, contact, city):  # __init__ initializer, constructor (other lang)
        self.rollNo = roll
        self.name = name
        self.contact = contact
        self.city = city

    def get_city(self):
        return self.city

    def update_contact(self, city_code):
        self.contact = city_code + "-" + self.contact


# # main script
stud1 = Student(1, "Sachin", "11111", "Mumbai")

print("-"*20)
# Access Attributes using an object
print(type(stud1))  # <class '__main__.Student'>
print(stud1.name)
print(stud1.rollNo)
print(stud1.city)

print("-"*20)
stud2 = Student(2, "Rahul", "22222", "Bengaluru")
print(type(stud2))
print(stud2.name)
print(stud2.rollNo)
print(Student.get_city(stud2))

print("-"*20)
# Adding property at object level :: for stud1
print("stud1 before adding marks: ", stud1.__dict__)
# print(stud1.marks)    # error before adding the property

stud1.marks = 80
print("New property for stud1", stud1.marks)
print("stud1 after adding marks: ", stud1.__dict__)
# print("Marks for stud2", stud2.marks)
print("stud2 after adding marks: ", stud2.__dict__)

# Deleting property at object level :: for stud2
del stud2.city  # remove property at object level, removed for stud2 only
# print(stud2.city) # AttributeError: 'Student' object has no attribute 'city'
print(stud2.name)
print("stud2 after deleting marks: ", stud2.__dict__)

# Deleting the object itself
del stud1       # Deleting the object itself, stud1 deleted
# print(stud1.name)
