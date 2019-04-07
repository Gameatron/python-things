class Dog:
    def __init__(self, breed, gender, age):
        self.breed = breed
        self.gender = gender
        self.age = age
        self.name = name
    
    def __str__(self):
        return f"You have a {self.age} year old {self.gender}, {self.breed} dog."

class Cat:
    def __init__(self, color, has_short_hair, gender, age, name):
        self.color = color
        self.has_short_hair = has_short_hair
        self.gender = gender
        self.age = age
        self.name = name
    
    def __str__(self):
        if self.has_short_hair.lower() == "yes":
            hair_type = "short haired"
        else:
            hair_type = "long haired"
        return f"You have a {self.age} year old {self.gender}, {self.color}, {hair_type} cat, named {self.name}."

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"You have a {self.age} year old pig named {self.name}."
    
def main():
    animal = input("Dog, Cat, or Pig? > ")
    if animal.lower() == "dog":
        breed = input("Breed? > ")
        gender = input("Gender? > ")
        age = input("How old? > ")
        dog = Dog(breed, gender, age)
        print(dog)
    
    elif animal.lower == cat:
        color = input("What color? > ")
        hair = input("Short hair - yes or no? > ")
        gender = input("Gender? > ")
        age = input("How old? > ")
        name = input("Name? > ")
        cat = Cat(color, hair, gender, age, name)
        print(cat)
    
    elif animal.lower == pig:
        name = input("Name? > ")
        age = input("How old? > ")
        pig = Pig(name, age)
        print(pig)

if __name__ == "__main__":
    main()