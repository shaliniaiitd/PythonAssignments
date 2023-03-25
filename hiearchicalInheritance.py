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


class Teacher(Person):

    def __init__(self, firstname, lastname, city, contact, exp):
        super().__init__(firstname, lastname, city, contact)
        self.exp = exp

    def change_exp(self, exp):
        self.exp = exp

    def read_exp(self):
        return self.exp


# main script
stud1 = Student("Sunil", "Gavaskar", "Mumbai", 55555, "Python")
stud2 = Student(firstname="Kapil", lastname="Dev", city="Chandigarh", contact=77777, program_lang="Java")

stud1.display_fullname()
print(stud1.program_lang)

stud2.display_fullname()

t1 = Teacher('Sunil', "B", "Pune", 88888, 20)
t1.display_fullname()
print("Exp", t1.read_exp())
t1.change_exp(25)
print("Exp", t1.read_exp())