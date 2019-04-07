from random import randint
class Character:
    def __init__(self, name, weapon, level):
        self.name = name
        self.weapon = weapon
        self.level = level
        self.hp = 30 + self.level * 20
    
    def attack(self, target):
        attack = self.weapon.attack()
        print(f"{self.name} attacked {target.name} with a {self.weapon.name} for {attack} damage!")
        target.hp -= attack
    
    def heal(self):
        self.hp += 10
        print(f"{self.name} is healing...")
    
    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True
    
    def __str__(self):
        return f"{self.name}:\nCurrent Weapon: {self.weapon}\n\tLevel: {self.level}\n"

class Weapon:
    def __init__(self, name, crit, ap):
        self.name = name
        self.crit = crit
        self.ap = ap
    
    # Calculates the damage that the weapon does for a character's attack
    def attack(self):
        ran_num = randint(1, 100)
        if ran_num <= self.crit:
            print("CRITICAL STRIKE!")
            return randint(self.ap+1, self.ap*2)

        elif ran_num <= 1:
            print(f"Your {self.name} glanced the foe!")
            return randint(1, self.ap//2)
        else:
            return randint(self.ap//2, self.ap)

    def __str__(self):
        return f"{self.name}\n\tDamage: {str(self.ap)}\n\tCritical Strike Chance: {str(self.crit)}%"

class Game:
    def __init__(self):
        self.hero_weapon = Weapon("Master Sword", 25, 12)
        self.hero = Character("Link", self.hero_weapon, 2)
        self.enemy_weapon = Weapon("Giant Club", 35, 8)
        self.enemy = Character("Ganon", self.enemy_weapon, 1)
    
    def play(self):
        i = 0
        while True:
            random_num = randint(1,100)
            i += 1
            print(f"Round {i}...")
            if random_num <= 50:
                print(f"{self.hero.name} HP: {self.hero.hp}\t{self.enemy.name} HP: {self.enemy.hp}")
                turn = input("Would you like to (h)eal or (a)ttack?\n> ")
                while True:
                    if turn.lower() == "attack" or turn.lower() == "a":
                        self.hero.attack(self.enemy)
                        break
                    elif turn == "heal" or turn == "h":
                        self.hero.heal()
                        break
                    else:
                        turn = input("That is not a valid input! Please enter one of the given options...\n> ")

                if self.enemy.hp < 20:
                    rand_num = randint(1,100)
                    if rand_num <= 50:
                        self.enemy.heal()
                    else:
                        self.enemy.attack(self.hero)
                else:
                    self.enemy.attack(self.hero)
                print(f"{self.hero.name} HP: {self.hero.hp}\t{self.enemy.name} HP: {self.enemy.hp}\n")
                if self.hero.is_alive() == False:
                    print(f"{self.enemy.name} has killed {self.hero.name} with its {self.enemy.weapon.name}!")
                    break
                elif self.enemy.is_alive() == False:
                    print(f"{self.hero.name} has killed {self.enemy.name} with its {self.hero.weapon.name}!")
                    break
                input("Press enter when you are ready to continue!")
                
            else:
                print(f"{self.hero.name} HP: {self.hero.hp}\t{self.enemy.name} HP: {self.enemy.hp}")
                if self.enemy.hp < 20:
                    rand_num = randint(1,100)
                    if rand_num <= 50:
                        self.enemy.heal()
                    else:
                        self.enemy.attack(self.hero)
                else:
                    self.enemy.attack(self.hero)

                turn = input("Would you like to (h)eal or (a)ttack?\n> ")
                while True:
                    if turn.lower() == "attack" or turn.lower() == "a":
                        self.hero.attack(self.enemy)
                        break
                    elif turn == "heal" or turn == "h":
                        self.hero.heal()
                        break
                    else:
                        turn = input("That is not a valid input! Please enter one of the given options...\n> ")

                print(f"{self.hero.name} HP: {self.hero.hp}\t{self.enemy.name} HP: {self.enemy.hp}\n")
                if self.hero.is_alive() == False:
                    print(f"{self.hero.name} has killed {self.enemy.name} with its {self.hero.weapon.name}!")
                    break
                elif self.enemy.is_alive() == False:
                    print(f"{self.enemy.name} has killed {self.hero.name} with its {self.enemy.weapon.name}!")
                    break
                input("Press enter when you are ready to continue!")
                print("\n\n\n\n\n\n\n\n\n\n\n\n")

        

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
