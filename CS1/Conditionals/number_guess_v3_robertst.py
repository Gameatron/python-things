def num_guess():
    secret = 7
    tries = 0
    print("""I am thinking of a number between one and ten
Can you guess it?""")
    guess = int(input(">"))
    
    while guess != secret:
        tries += 1
        if guess > secret:
            print("Nope, too high.")
            guess = int(input(">"))
        else:
            print("Nope, too low.")
            guess = int(input(">"))
    print(f"You got it! It only took you {tries} tries.")

def main():
    num_guess()

if __name__ == "__main__":
    main()