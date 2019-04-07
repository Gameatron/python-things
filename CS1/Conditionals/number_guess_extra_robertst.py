#my way of solving:
    #first hit 3, if too high then go lower, if low, then hit 7
    #if 7 is too low then go higher. if too high then go lower


from random import randint

def num_guess(d):
    if d == "easy":
        secret = randint(1, 10)
        max_tries = 4
    elif d == "medium":
        secret = randint(1, 100)
        max_tries = 7
    elif d == "hard":
        secret = randint(1, 1000)
        max_tries = 10
    tries = 1
    print("""I am thinking of a number between one and ten
Can you guess it?""")
    guess = int(input(">"))
    
    while tries < max_tries and guess != secret:
        tries += 1
        if guess > secret:
            print("Nope, too high.")
            guess = int(input(">"))
        else:
            print("Nope, too low.")
            guess = int(input(">"))
    if guess == secret:
        print(f"Good job, it only took you {tries} tries!")
    else:
        print(f"Too bad, the number was {secret}")
    
        
def main():
    difficulty = input('Please choose a difficulty ("easy", "medium", "hard") ')
    if difficulty == "easy":
        num_guess("easy")
    elif difficulty == "medium":
        num_guess("med")
    elif difficulty == "hard":
        num_guess("hard")

if __name__ == "__main__":
    main()