def two_questions():
    # Six possible items are:
    #     Horse, sparrow, carrot, rose bush, car, and phone charger.
    
    print("Welcome to:\n   Two Questions!!\nThink of an object, and I will try to guess it.")
    q_one = input("\nQuestion One) Is it an animal, vegetable, or mineral? ")
    q_two = input("\nQuestion Two) Is it bigger than a breadox? ")

    if q_one == "animal" or q_one == "Animal":
        if q_two == "yes" or q_two == "Yes":
            print("You're thinking of a horse!")
        elif q_two == "no" or q_two == "No":
            print("You're thinking of a sparrow!")
        else:
            print("Sorry, couldn't quite catch that.")
        
    elif q_one == "vegetable" or q_one == "Vegetable":
        if q_two == "yes" or q_two == "Yes":
            print("You're thinking of a rose bush!")
        elif q_two == "no" or q_two == "No":
            print("You're thinking of a carrot!")
        else:
            print("Sorry, couldn't quite catch that.")

    elif q_one == "mineral" or q_one == "Mineral":
        if q_two == "yes" or q_two == "Yes":
            print("You're thinking of a car!")
        elif q_two == "no" or q_two == "No":
            print("You're thinking of a phone charger!")
        else:
            print("Sorry, couldn't quite catch that.")
    
    else:
        print("I hope you know, those aren't actually answers.")

if __name__ == "__main__":
    two_questions()