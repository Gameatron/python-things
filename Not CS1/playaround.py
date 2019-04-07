class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hug(self, targ):
        print(f"{self.name} hugs {targ.name}!")
    
    def __str__(self):
        return f"{self.name} is a branch of person who is  {self.age} years old!"

def main():
    koda = Person("Koda", 16)
    willow = Person("Willow", 17)
    print(koda)
    print(willow)

if __name__ == "__main__":
    main()