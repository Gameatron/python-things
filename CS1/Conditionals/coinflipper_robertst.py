import random
#This program is an example of using a programming technique
#called "loop and a half". It's pretty cool and very useful.
#You will need o use quite a few of these for your choose your
#own adventure game.

def coinflip():
    ''' Flip a "coin", keeping track of how many in a row were
        heads. Allows the user to coose wether or not to continue.
        If heads is not flipped the program ends.
    '''
    # initialize the streak counter
    streak = 0
    
    #start an "infinite loop"
    while True:
        
        #get a random number between 0 and 1. If the number is
        # less than 0.5, treat it as heads, otherwise treat it as
        # tails. This is a "fair: coin (50/50 heads/tails)
        gotHeads = random.random() < 0.5
        if gotHeads:
            coin = "Heads"
        else:
            coin = "Tails"
            
        #display the results of the "coin" toss
        print("You flip a coin and it is..." + coin)
        
        # If heads was flipped, increment the counter
        # and give the player the option to flip again.
        #Otherwise end the game and set the streak back
        # to 0.
        if gotHeads:
            streak += 1
            print(f"\tThat's {streak} in a row...")
            again = input("\tWould you like to flip again (y/n)? ")
        else:
            print("\tYou lose everything!")
            print("\tShould've quit while you were aHEAD....")
            streak = 0
            again = "n"
        # If the player chose not to flip again, or if they
        # didn't roll a heads, end the infinite loop
        # using the "break" key word.
        if again != "y":
            break
    
    # After the while loop... either the player chose not to
    # flip again, OR they lost... either way, print the score.
    print(f"Final score: {streak}")

if __name__ == "__main__":
    coinflip()
    