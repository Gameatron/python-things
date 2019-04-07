def little_quiz():
    score = 0
    
    #greeting
    print("\t\tWelcome to the Skyrim quiz!")
    
    #question 1
    print("Who is the main antagonist?")
    print("\tA. Alduin")
    print("\tB. Ulfric Stormcloack")
    print("\tC. Miraak")
    answer1 = input("> ")
    if answer1 == "A":
        print("That is the correct answer!")
        score += 33.33
    else:
        print("That is the incorrect answer.")
    
    #question 2
    print("\nWhat are the two sides of the civil war?")
    print("\tA. The bears Vs. The Hawks")
    print("\tB. The Stormcloacks Vs. the Empire")
    print("\tC. The dragons Vs. the warriors")
    answer2 = input("> ")
    if answer2 == "B":
        print("That is the correct answer!")
        score += 33.33
    else:
        print("That is the incorrect answer.")
    
    #question 3
    print("\nWho is the main character?")
    print("\tA. Miraak")
    print("\tB. Dragonborn")
    print("\tC. Brandon")
    answer3 = input("> ")
    if answer3 == "B":
        print("That is the correct answer!")
        score += 33.34
    else:
        print("That is the incorrect answer.")
    
    print(f'\nYou got a score of {score}%')
    if score == 100:
        print("You got a perfect score!")
    else:
        print("Better luck next time.")

def main():
    little_quiz()

if __name__ == "__main__":
    main()