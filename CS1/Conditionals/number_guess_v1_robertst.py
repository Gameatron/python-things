def num_guess():
    secret = 
    print("""I am thinking of a number between one and ten
Can you guess it?""")
    guess = int(input(">"))
    
    while guess != secret:
        print("Nope, Try again.")
        guess = int(input(">"))
    print("Yep, you got it!")

def main():
    num_guess()

if __name__ == "__main__":
    main()