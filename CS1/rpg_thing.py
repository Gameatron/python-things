class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = self.level * 20 + 30

    def attack(self, enemy):
        pass

class Application:
    def __init__(self):
        pass
    
    def run(self):
        print('f')

if __name__ == "__main__":
    game = Application()
    game.run()