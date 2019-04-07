def num_guess():
    secret = 7
    tries = 1
    print("""I am thinking of a number between one and ten
Can you guess it?""")
    guess = int(input(">"))
    
    while guess != secret and tries < 3:
        tries += 1
        if guess > secret:
            print("Nope, too high.")
            guess = int(input(">"))
        elif guess < secret:
            print("Nope, too low.")
            guess = int(input(">"))
        if tries > 3:
            print(f"Too bad, the number was {secret}")
        if tries <= 3 and guess == secret:
            print(f"Good job, it only took you {tries} tries!")
        
        
def main():
    num_guess()

if __name__ == "__main__":
    main()