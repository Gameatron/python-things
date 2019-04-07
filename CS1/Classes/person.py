class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.firstname} {self.lastname}, {self.age} years old"

    def underage(self):
        return self.age < 18


class Student(Person):
    def __init__(self, firstname, lastname, age, endorsement):
        super().__init__(firstname, lastname, age)
        self.courselist = []
        self.endorsement = endorsement

    def find_year(self):
        return f"Year {self.age - 11}"

    def underage(self):
        return self.age < 21

    def enroll(self, course):
        self.courselist.append(course)


class Parent(Person):
    def __init__(self, firstname, lastname, age, occupation):
        super().__init__(firstname, lastname, age)
        self.occupation = occupation
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def list_children(self):
        print(f"{self.firstname} {self.lastname} has {len(self.children)} children:")
        for child in self.children:
            print("  ", child)

    def __str__(self):
        return f"{self.firstname} {self.lastname}, {self.age} years old, {self.occupation}"


def main():
    arthur = Parent("Arthur", "Weasley", 48, "Muggle Studies")
    ron = Student("Ron", "Weasley", 14, "Potions")
    fred = Student("Fred", "Weasley", 16, "Charms")
    george = Student("George", "Weasley", 16, "Herbology")
    ginny = Student("Ginny", "Weasley", 13, "Divination")
    arthur.add_child(ron)
    arthur.add_child(fred)
    arthur.add_child(george)
    arthur.add_child(ginny)
    arthur.list_children()


if __name__ == "__main__":
    main()
