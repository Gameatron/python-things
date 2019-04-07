class Dog:
    def __init__(self, breed, gender, age, name):
        self.breed = breed
        self.gender = gender
        self.age = age
        self.name = name
        # self.is_sitting = is_sitting
    
    def __str__(self):
        return f"I am a {self.age} year old {self.gender} {self.breed} named {self.name}."
    
    def play(self):
        print("I am playing fetch!")
    
    def bark(self, amount):
        for _ in range(amount):
            print("BARK!")
            
    #def sit(self):
       # if self.is_sitting == False:
        #    self.is_sitting = True
        #    print("I sat down!")
       # else:
        #    return
        
class Kennel:
    def __init__(self, num_cages):
        self.num_cages = num_cages
        self.dogs = []
    
    def add_dog(self, dog):
        if len(self.dogs) < self.num_cages:
            self.dogs.append(dog)
            print("One dog added to the kennel.")
        else:
            print("Sorry, the kennel is full!")
        
    def list_dogs(self):
        for dog in self.dogs:
            print(dog)
    
def main():
    my_kennel = Kennel(2)
    my_kennel.add_dog(Dog("great dane", "male", 1, "Astro"))
    my_kennel.add_dog(Dog("golden retriever", "male", 10, "Dug"))
    my_kennel.add_dog(Dog("beagle", "male", 12, "Snoopy"))
    my_kennel.list_dogs()
    
    
if __name__ == "__main__":
    main()
