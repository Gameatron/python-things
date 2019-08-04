import time

"""
                                        1
                        2                               3
                4               5               6               7
            8       9       10      11      12      13      14      15
                        
"""


class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = level * 20 + 30


class Game:
    def __init__(self):
        pass

    def intro(self):
        name = input(
            "Welcome to Koda's adventure game!\nBefore I begin the story, what is your character's name?\n> ").capitalize()
        hero = Character(name, 1)
        print(f"\nAnd now, {hero.name}'s adventure begins.")
        for _ in range(3):
            print('.', end='', flush=True)
            time.sleep(1)
        print()
        return hero

    def part1(self, hero):
        ans = input(f"""{hero.name} wakes up, locked in chains. 
They spot a key within view, but can't see any visible way to get it. 
\tWould they (s)truggle, or (w)ait?\n> """).lower()
        while True:
            if ans == 's' or ans == 'w':
                break
            else:
                ans = input(f"That is not a valid option. {hero.name} can only (w)ait, or (s)truggle.\n> ")
        return ans
    
    def part2(self, hero):
        ans = input(f"""{hero.name} decided to wait.
While {hero.name} is waiting, they hear footsteps coming from a nearby hall.
As the steps come nearer and nearer, a man peeks around the corner.
He gently says to {hero.name}, 'Ah, I see you are awake! Just in time...'.
\tWould the hero attempt to (e)scape, or (w)ait?\n> """).lower()
        while True:
            if ans == 'e' or ans == 'w':
                break
            else:
                ans = input("That is not a valid choice, please choose (e) or (w).").lower()
        return ans

    def part3(self, hero):
        ans = input(f"""{hero.name} decides to struggle.
They gently pull at the chains that are binding them, then suddenly tug.
The chain pulls off, almost miraculously.
{hero.name} slowly stands up, brushing themselves off.
A strange man slowly walks into the room, grabbing a knife when they see the hero has escaped the binds.
\tDoes {hero.name} decide to (r)un, or (f)ight?""").lower()
        while True:
            if ans == 'r' or ans == 'f':
                break
            else:
                ans = input("That is not a valid choice, please choose (r) or (f).").lower()
        return ans
    
    def part4(self, hero):
        ans = input(f"""{hero.name} has decided to attempt an escape!
They make a run for the hall, taking a sharp turn.""")

    def main(self):
        hero = self.intro()
        ans = self.part1(hero)
        if ans == 'w':
            ans = self.part2(hero)
            if ans == 'e':
                ans = self.part4(hero)
                if ans == None:
                    ans = self.part8(hero)
                elif ans == None:
                    ans = self.part9(hero)
            elif ans == 'w':
                ans = self.part5(hero)
                if ans == None:
                    ans = self.part10(hero)
                elif ans == None:
                    ans = self.part11(hero)
        elif ans == 's':
            ans = self.part3(hero)
            if ans == None:
                ans = self.part6(hero)
                if ans == None:
                    ans = self.part12(hero)
                elif ans == None:
                    ans = self.part13(hero)
            elif ans == None:
                ans = self.part7(hero)
                if ans == None:
                    ans = self.part14(hero)
                elif ans == None:
                    ans = self.part15(hero)


if __name__ == "__main__":
    game = Game()
    game.main()
