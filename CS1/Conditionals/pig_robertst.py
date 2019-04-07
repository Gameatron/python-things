from random import randint

def play_pig():
    round_score = 0
    while True:
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        print(dice1, dice2)
        if dice1 == 1 and dice2 == 1:
            round_score += 25
        elif dice1 == dice2:
            round_score += (dice1+dice2)*2
        elif dice1 == 1 or dice2 == 1:
            round_score = 0
            break
        else:
            round_score += (dice1 + dice2)
        cont = input("Would you like to 'roll' again, or 'hold'? ")
        if cont == "roll":
            pass
        elif cont == "hold":
            break
    print(f"You scored {round_score} points this round!")
        

if __name__ == "__main__":
    play_pig()