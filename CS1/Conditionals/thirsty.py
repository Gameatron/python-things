def to_drink():
    print("Welcome to my house!\nWould you like something to drink? ")
    thirsty = input("> ")
    if thirsty == "yes":
        print("Great! Would you like water, OJ, soda, or purple stuff? ")
        what = input("> ")
        if what == "water":
            print("Drink 8 glasses a day!")
        elif what == "OJ":
            print("If the glove don't fit, you must acquit!")
        elif what == "soda":
            print("Bad choice! That stuff is full of sugar.")
        elif what == "purple stuff":
            print("Purple stuff = Barney + Blender")
        else:
            print(f"Sorry, I'm all out of {what}. :(")

    elif thirsty == "no":
        print("Oh...well fine then, be that way!")
        
    else:
        print("Sorry, didn't catch that.")

if __name__ == "__main__":
    to_drink()