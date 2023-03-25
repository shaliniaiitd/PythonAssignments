class Person:
    """Person Class definition"""
    studies = False

    def __init__(self, firstname, lastname, city, contact):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.contact = contact

    def display_fullname(self):
        print("Full Name is %s %s, city is %s" % (self.firstname, self.lastname, self.city))

    def change_city(self, city):
        self.city = city

    def read_city(self):
        return self.city


class Student(Person):
    studies = True

    def __init__(self, firstname, lastname, city, contact, program_lang):
        super().__init__(firstname, lastname, city, contact)
        self.program_lang = program_lang


class TestingStudent(Student):

    def __init__(self, firstname, lastname, city, contact, program_lang, tool):
        super().__init__(firstname, lastname, city, contact, program_lang)
        self.tool = tool

    def change_tool(self, tool):
        self.tool = tool

    def read_tool(self):
        return self.tool


# main script
stud1 = Student("Sunil", "Gavaskar", "Mumbai", 55555, "Python")
stud2 = Student(firstname="Kapil", lastname="Dev", city="Chandigarh", contact=77777, program_lang="Java")

stud1.display_fullname()
print(stud1.program_lang)

stud2.display_fullname()

test_stud = TestingStudent("Karan", "Dave", "Pune", 99999, "Python", "Selenium")
test_stud.display_fullname()
print("Tool", test_stud.read_tool())
test_stud.change_tool("Postman")
print("Tool", test_stud.read_tool())