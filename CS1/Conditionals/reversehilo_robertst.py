def hi_lo():
    lo = 1
    hi = 1000
    ans = ""
    print("Think of a number you want me to guess.")
    while ans != "c":
        guess = (lo + hi) // 2
        ans = input(f'\nMy guess is {guess}. Am I too (l)ow, (h)igh, or (c)orrect? ')
        if guess == 999 and ans == "l":
            lo = 1000
        elif ans == "l":
            lo = guess
        elif ans == "h":
            hi = guess
    print("Yay! I am the best guesser!!")

def main():
    hi_lo()

if __name__ == "__main__":
    main()