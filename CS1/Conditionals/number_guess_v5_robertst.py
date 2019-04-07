#my way of solving:
    #first hit 3, if too high then go lower, if low, then hit 7
    #if 7 is too low then go higher. if too high then go lower


from random import randint

def num_guess():
    secret =randint(1, 10)
    tries = 1
    print("""I am thinking of a number between one and ten
Can you guess it?""")
    guess = int(input(">"))
    
    while guess != secret and tries < 4:
        tries += 1
        if guess > secret:
            print("Nope, too high.")
            guess = int(input(">"))
        elif guess < secret:
            print("Nope, too low.")
            guess = int(input(">"))
        if tries <= 4 and guess == secret:
            print(f"Good job, it only took you {tries} tries!")
    if tries == 4:
        print(f"Too bad, the number was {secret}")
        
        
def main():
    num_guess()

if __name__ == "__main__":
    main()