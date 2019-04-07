from random import randint

def play_round():
    # Runs a single round of pig and returns the round score
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
        cont = input("'roll' or 'hold'? >")
        if cont == "roll":
            pass
        elif cont == "hold":
            break
    print(f"Round score: {round_score}")
    return round_score

def play_pig(win_score):
    """ Plays a multi-round game of Pig, keeping track of the overall
        score. When the player's score gets to win_score, the game
        will end.
    """
    score = 0
    while score < win_score:
        input("Press 'enter' when it is your turn")
        score += play_round()
        print(f"Overall score: {score}")
        
if __name__ == "__main__":
    play_pig(69420)