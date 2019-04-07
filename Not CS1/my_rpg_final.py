from random import randint, choice
from time import sleep


class Character:
    def __init__(self, name, weapon, level):
        self.name = name
        self.weapon = weapon
        self.level = level
        self.lvl_end = 15
        self.exp = 0
        self.max_hp = 30 + self.level * 20
        self.hp = 30 + self.level * 20

    def attack(self, target):
        attack = self.weapon.attack()
        print(
            f"{self.name} attacked {target.name} with a {self.weapon.name} for {attack} damage!")
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

    def level_up(self):
        if self.exp > self.lvl_end:
            print(
                f"{self.name} has reached level {self.level}! You need {self.lvl_end-self.exp} to level up again!")
            self.level += 1
            self.max_hp += 20
            self.lvl_end **= 2
        else:
            print(f"You need {self.lvl_end-self.exp} experience to level up!")


class Weapon:
    def __init__(self, name, crit, ap):
        self.name = name
        self.crit = crit
        self.ap = ap

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


class Spell(Weapon):
    def __init__(self, name, crit, ap, element):
        super().__init__(name, crit, ap)
        self.element = element

    def attack(self):
        ran_num = randint(1, 100)
        if ran_num <= self.crit:
            print("CRITICAL STRIKE!")
            return self.ap*2
        else:
            return self.ap


class Staff(Weapon):
    def __init__(self, name, crit, ap, healing):
        super().__init__(name, crit, ap)
        self.healing = healing

    def attack(self):
        ran_num = randint(1, 100)
        if ran_num < 10:
            return self.healing
        else:
            ran_num = randint(1, 100)
            if ran_num <= self.crit:
                print("CRITICAL STRIKE!")
                return randint(self.ap/2, self.ap)*2
            else:
                return randint(self.ap/2, self.ap)


class Firearm(Weapon):
    def __init__(self, name, crit, ap, ammo, reload_time):
        super().__init__(name, crit, ap)
        self.ammo = ammo
        self.max_ammo = ammo
        self.reload_time = reload_time
        self.reloading_to_done = reload_time
        self.is_reloading = False
        if self.max_ammo <= 10:
            self.fire_rate = 1
            self.typeof = "single"
        else:
            self.fire_rate = 5
            self.typeof = "full"

    def attack(self):
        ran_num = randint(1, 100)
        if ran_num <= self.crit:
            print("CRITICAL STRIKE!")
            if self.typeof == 'single':
                return randint(self.ap+1, self.ap*2)
            elif self.typeof == "full":
                return randint(self.ap+1, self.ap*2)*self.fire_rate
        else:
            if self.typeof == 'single':
                return randint(self.ap//2, self.ap)
            elif self.typeof == "full":
                return randint(self.ap//2, self.ap)*self.fire_rate


class Mage(Character):
    def __init__(self, name, weapon, spell, level):
        super().__init__(name, weapon, level)
        self.spell = spell

    def cast(self, target):
        attack = self.spell.attack()
        print(f"{self.name} casts {self.spell.name} on {target.name} for {attack} {self.spell.element} damage!")
        target.hp -= attack


class Warrior(Character):
    def __init__(self, name, weapon, level):
        super().__init__(name, weapon, level)
        self.is_charging = False

    def charge_up(self):
        self.is_charging = True
        print(f"{self.name} is charging an attack!")

    def attack(self, target):
        attack = self.weapon.attack()
        if self.is_charging == True:
            print(f"{self.name} uses a charged attack!")
            print(
                f"{self.name} attacked {target.name} with a {self.weapon.name} for {attack*2} damage!")
            target.hp -= attack*2
            self.is_charging = False
        else:
            print(
                f"{self.name} attacked {target.name} with a {self.weapon.name} for {attack} damage!")
            target.hp -= attack


class Cleric(Character):
    def __init__(self, name, weapon, level):
        super().__init__(name, weapon, level)
        self.bonus_heal = level * 15
        self.hp += 20

    def attack(self, target):
        attack = self.weapon.attack()
        if attack < 1:
            print(f"{self.name}'s staff healed its owner for {abs(attack)} HP!")
            self.hp -= attack
        else:
            print(
                f"{self.name} attacked {target.name} with a {self.weapon.name} for {attack} damage!")
            target.hp -= attack

    def heal(self):
        if randint(1, 100) < 90:
            print(
                f"{self.name} is using powerful healing magic...\nThey gain {self.bonus_heal} health!")
            self.hp += self.bonus_heal
        else:
            print(f"{self.name} is using powerful healing magic...\nIt was super effective!! They gain {self.bonus_heal*1.5} health!")
            self.hp += self.bonus_heal*1.5


class Gunslinger(Character):
    def __init__(self, name, weapon, level):
        super().__init__(name, weapon, level)

    def reload(self):
        print(f"{self.name} is reloading his {self.weapon.name}...")
        self.weapon.reloading_to_done -= 1
        if self.weapon.reloading_to_done == 0:
            print(f"{self.name} is done reloading!")
            self.is_reloading = False
            self.weapon.ammo = self.weapon.max_ammo

    def oof(self):
        self.hp += 12098230948048239
        print('oof')

    def attack(self, target):
        if self.weapon.ammo == 0:
            self.weapon.is_reloading = True
        if self.weapon.is_reloading == True:
            self.reload()

        else:
            attack = self.weapon.attack()
            print(
                f"{self.name} shoots {target.name} with its {self.weapon.name} for {attack} damage!")
            self.weapon.ammo -= self.weapon.fire_rate
            target.hp -= attack


class Game:
    def __init__(self):
        self.spells = []
        self.weapons = []
        self.plans = []
        self.staffs = []
        self.guns = []
        self.spells.append(Spell("Fireball", 0, 20, "fire"))  # 0
        self.spells.append(Spell("Ice Sheets", 0, 20, "ice"))  # 1
        self.weapons.append(Weapon("Big Sword", 30, 15))  # 0
        self.weapons.append(Weapon("Magic Wand", 50, 10))  # 1
        self.weapons.append(Weapon("Battle Axe", 10, 20))  # 2
        self.staffs.append(Staff("Staff of Great Healing", 20, 10, -25))  # 0
        self.staffs.append(Staff("Staff of Regular Healing", 10, 20, -15))  # 1
        self.guns.append(Firearm("Bazooka", 5, 40, 1, 2))  # 0
        self.guns.append(Firearm("Assault Rifle", 30, 5, 10, 1))  # 1
        self.guns.append(Firearm("Revolver", 30, 10, 5, 2))  # 2

    def startup(self):
        print("Welcome to My RPG!")
        name = input("Enter your name: ")
        while True:
            job = input(
                "(W)arrior, (M)age, (C)leric, or (G)unslinger: ").lower()
            if job == 'w' or job == 'm' or job == 'c' or job == 'g':
                break
            else:
                print("Invalid choice.  Enter M, W, C, or G.")

        if job == 'w':
            while True:
                weapon = input("Do you want a (s)word or an (a)xe? ").lower()
                if weapon == 's':
                    weapon = 0  # this order matters!
                    break
                elif weapon == 'a':
                    weapon = 2  # this order matters!
                    break
                else:
                    print("Invalid choice. Enter S or A.")

            print("Creating your warrior...")
            self.hero = Warrior(name, self.weapons[weapon], 1)

        elif job == 'c':
            while True:
                staff = input(
                    "Do you want a staff of (G)reater healing, or a Staff of (N)ormal Healing? ").lower()
                if staff == 'g':
                    staff = 0
                    break
                elif staff == 'n':
                    staff = 1
                    break
                else:
                    print("Invalid choice. Enter G or N.")

            print("Creating your cleric...")
            self.hero = Cleric(name, self.staffs[staff], 1)

        elif job == 'm':
            while True:
                spell = input(
                    "Do you want to use (f)ire magic or (i)ce magic? ").lower()
                if spell == 'f':
                    spell = 0  # this matters!
                    break
                elif spell == 'i':
                    spell = 1  # this matters!
                    break
                else:
                    print("Invalid choice. Enter F or I.")

            print("Creating your mage...")
            self.hero = Mage(name, self.weapons[1], self.spells[spell], 1)

        elif job == 'g':
            while True:
                weapon = input(
                    "Do you want a (B)azooka, (A)ssault Rifle, or (R)evolver? ").lower()
                if weapon == 'b':
                    weapon = 0
                    break
                elif weapon == 'a':
                    weapon = 1
                    break
                elif weapon == 'r':
                    weapon = 2
                    break
                else:
                    print("Invalid choice. Enter B, A, or R.")

            print("Creating your gunslinger...")
            self.hero = Gunslinger(name, self.guns[weapon], 1)

        print(f"Welcome to the world, {self.hero.name}!")
        print("Press enter when you're ready to begin!")
        input()

    def gen_enemy(self):
        ran_num = randint(0, 3)
        if ran_num == 1:
            spell = choice(list(self.spells))
            return Mage("Mage", self.weapons[1], spell, self.hero.level)
        elif ran_num == 2:
            staff = choice(list(self.staffs))
            return Cleric("Cleric", staff, self.hero.level)
        elif ran_num == 3:
            weapon = choice(list(self.guns))
            return Gunslinger("Gunslinger", weapon, self.hero.level)
        else:
            weapon = choice(list(self.weapons))
            return Warrior("Warrior", weapon, self.hero.level)

    def play(self):
        print(f"Your status:\nCurrent Level:{self.hero.level}")
        print(f"Current HP:{self.hero.hp}")
        print("Generating an enemy.", end='')
        for _ in range(3):
            sleep(1)
            print(".", end='')
        print()
        enemy = self.gen_enemy()
        print(
            f"It looks like you will be fighting a level {enemy.level} {enemy.name}!")
        input("Fight!")
        round_num = 1
        while self.hero.is_alive() and enemy.is_alive():
            print(f"Round {round_num}:")
            self.fight_round(enemy)
            print(f"Player HP: {self.hero.hp}\t\t{enemy.name} HP: {enemy.hp}")
            round_num += 1
            print()

        if self.hero.is_alive():
            print(
                f"It looks like {self.hero.name} lives to fight another day!")
            self.hero.exp += enemy.level*10
            self.hero.level_up()

    def enemy_turn(self, enemy):
        if type(enemy) == Warrior:
            # enemy is healthy options
            if enemy.hp > 20:
                # charge up sometimes if not already charging
                if randint(1, 5) < 3 and not enemy.is_charging:
                    enemy.charge_up()
                else:
                    enemy.attack(self.hero)
            else:
                # enemy has low health
                if randint(0, 1) == 1:
                    enemy.heal()
                else:
                    enemy.attack(self.hero)

        elif type(enemy) == Mage:
            # enemy is healthy options
            if enemy.hp > 20:
                if randint(1, 5) < 2:
                    enemy.attack(self.hero)
                else:
                    enemy.cast(self.hero)
            else:
                # enemy is low health
                if randint(0, 1) == 0:
                    enemy.heal()
                else:
                    enemy.cast(self.hero)

        elif type(enemy) == Cleric:
            if enemy.hp < 20:
                if randint(1, 100) < 75:
                    enemy.attack(self.hero)
                else:
                    enemy.heal()
            else:
                if randint(1, 100) < 50:
                    enemy.attack(self.hero)
                else:
                    enemy.heal()

        elif type(enemy) == Gunslinger:
            if enemy.hp < 20:
                if randint(1, 100) < 75:
                    enemy.attack(self.hero)
                else:
                    enemy.heal()
            else:
                if randint(1, 100) < 50:
                    enemy.attack(self.hero)
                else:
                    enemy.heal

    def player_turn(self, enemy):
        if type(self.hero) == Warrior:
            move = input(
                "Would you like to (A)ttack, (C)harge Up, or (H)eal? ").lower()
            if move == 'a':
                self.hero.attack(enemy)
            elif move == 'c':
                self.hero.charge_up()
            elif move == 'h':
                self.hero.heal()
            else:
                print("That wasn't an option! You lose your turn!")

        elif type(self.hero) == Mage:
            move = input(
                f"Would you like to (A)ttack, (C)ast {self.hero.spell.name}, or (H)eal? ").lower()
            if move == 'a':
                self.hero.attack(enemy)
            elif move == 'c':
                self.hero.cast(enemy)
            elif move == 'h':
                self.hero.heal()
            else:
                print("That wasn't an option! You lose your turn!")

        elif type(self.hero) == Cleric:
            move = input(
                f"Would you like to (A)ttack or (S)uper heal? ").lower()
            if move == 'a':
                self.hero.attack(enemy)
            elif move == 's':
                self.hero.heal()
            else:
                print("That wasn't an option! You lose your turn!")

        elif type(self.hero) == Gunslinger:
            move = input("Would you like to (A)ttack or (H)eal? ").lower()
            if move == 'a':
                self.hero.attack(enemy)
            elif move == 'h':
                self.hero.heal()
            elif move == 'oof':
                self.hero.oof()
            else:
                print("That wasn't an option! You lose your turn!")

    def fight_round(self, enemy):
        # Determine who goes first
        if randint(0, 1) == 1:
            # enemy goes first
            print(f"Player HP: {self.hero.hp}\t\t{enemy.name} HP: {enemy.hp}")
            self.enemy_turn(enemy)
            if self.hero.is_alive() == False:
                print(
                    f"{enemy.name} has killed {self.hero.name} with his {enemy.weapon.name}!")
                return
            self.player_turn(enemy)
            if enemy.is_alive() == False:
                return
        else:
            # player goes first
            print(f"Player HP: {self.hero.hp}\t\t{enemy.name} HP: {enemy.hp}")
            self.player_turn(enemy)
            if enemy.is_alive() == False:
                return
            self.enemy_turn(enemy)
            if self.hero.is_alive() == False:
                print(
                    f"{enemy.name} has killed {self.hero.name} with his {enemy.weapon.name}!")
                return


def main():
    game = Game()
    game.startup()
    game.play()


if __name__ == "__main__":
    main()
