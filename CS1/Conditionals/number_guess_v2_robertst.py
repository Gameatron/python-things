def num_guess():
    secret = 7
    print("""I am thinking of a number between one and ten
Can you guess it?""")
    guess = int(input(">"))
    
    while guess != secret:
        if guess > secret:
            print("Nope, too high.")
            guess = int(input(">"))
        elif guess < secret:
            print("Nope, too low.")
            guess = int(input(">"))
    print("Yep, you got it!")

def main():
    num_guess()

if __name__ == "__main__":
    main()