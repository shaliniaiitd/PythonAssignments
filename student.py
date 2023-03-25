class Student:  # PascalCase
    def __init__(self, roll, name, contact, city):  # __init__ initializer, constructor (other lang)
        self.rollNo = roll
        self.name = name
        self.contact = contact
        self.city = city
        # self.marks = 0      # defining marks property

    # self can be used within init or methods only
    # self.grade = "A"

    def get_city(self):
        return self.city

    def update_contact(self, city_code):
        self.contact = city_code + "-" + self.contact

    def take_exams(self, score):
        # print(self.marks) # Unresolved attribute reference 'marks' for class 'Student'
        self.marks = score  # instnace attribute marks defined outside __init__()

    # marks will be applicable/ available only if method take_exams() is called
    # marks will be applicable/ available only for the object for whom take_exams() was called
# # main script
stud1 = Student(1, "Sachin", "11111", "Mumbai")

print("-" * 20)
# Access Attributes using an object
print(type(stud1))  # <class '__main__.Student'>
print(stud1.name)
print(stud1.rollNo)
print(stud1.city)

print("-" * 20)
stud2 = Student(2, "Rahul", "22222", "Bengaluru")
print(type(stud2))
print(stud2.name)
print(stud2.rollNo)
print(Student.get_city(stud2))

print("-" * 20)
stud1.take_exams(70)
print(stud1.__dict__) knee c''
print(stud1.marks)
# print(stud2.marks)    # error