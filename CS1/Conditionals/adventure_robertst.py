def adventure():
    strikes = 1
    points = 0
    print("""Welcome to Koda\'s Dungeon Adventure!
    before I begin, what is your characters name?""")
    name = input(">")
    print(f"""Hello, {name}.
    {name} awakens lieing out in front of an extremely large opening to a cave.
    This place looks as though it has been here for many, many years.
    Does {name} want "explore" the caves or "look" around the entrance""")
    while True:
        pt1 = input(">")
        if pt1 == "explore" or pt1 == "look":
            break
        else:
            print('You must type "explore" or "look".')
            strikes += 1
        if strikes == 5:
            print(f"""{name} took too long to decide, and a dragon came and ate him.
    THE END""")
            return

    if pt1 == "explore":
        points += 1
        print(f"""{name} decides to explore the caves.
    {name} steps in to see a chest, and a continuous hallway.
    Does {name} wish to "open" the chest, or "continue" walking?""")
        while True:
            pt2 = input(">")
            if pt2 == "continue" or pt2 == "open":
                break
            else:
                print("You must type 'open' or 'continue'.")
                strikes += 1
            if strikes == 5:
                print(f"""{name} took too long to decide, and a dragon came and ate him.
    THE END""")
                return

        if pt2 == "continue":
            points += 2
            print(f"""{name} walks right past the treasure chest.
    After walking for about a minute {name} enters a chamber.
    Inside the chamber is a huge Ice Dragon, deep in sleep.
    Does {name} want to "poke" the dragon, or let it "sleep"?""")
            while True:
                pt4 = input(">")
                if pt4 == "poke" or pt4 == "sleep":
                    break
                else:
                    print("You must type 'poke' or 'sleep'.")
                    strikes += 1
                if strikes == 5:
                    print(f"""{name} took too long to decide, and a dragon came and ate him.
    THE END""")
                    return

            if pt4 == "poke":
                points += 1
                print(f"""\t{name} finds a nice, large stick and walk up to the dragon.
    {name} gets his stick aimed at its nostril.
    {name} goes in for the poke, and hit in right up the nostril.
    The dragon wakes up, roars, and eats {name}.
    THE END""")
            elif pt4 == "sleep":
                points += 3
                print(f"""\t{name} just decides to let the dragon sleep.
    In {name}'s attempt, he fell asleep as well.
    {name} wakes up to the dragons nose in his face.
    {name} just sits there, and then the dragon sits, and looks at him.
    {name} reaches up to pet it, and the dragon rolls over with its tongue sticking out.
    Looks like all it needed was a friend after all.
        THE END""")
        elif pt2 == "open":
            points += 2
            print(f"""{name} opens the chest, and in it he sees an eight hand-length longsword.
    {name} takes up the sword and inspect it closely.
    {name} does not see any damage or anything, but he thinks:
    "A gun would have been better." but this works good enough.
    would {name} like to "continue" or "leave"?""")
            while True:
                pt5 = input(">")
                if pt5 == "continue" or pt5 == "leave":
                    break
                else:
                    print("You must type 'continue' or 'leave'.")
                    strikes += 1
                if strikes == 5:
                    print(f"""{name} took too long to decide, and a dragon came and ate him.
    THE END""")
                    return

            if pt5 == "continue":
                points += 5
                print(f"""{name} decides to continue on through the caves.
    As {name} is going down he sees the caves begin to open up more.
    Near the end of the hall way {name} hears a large roar in the open area.
    {name} walk in to discover a dragon, that is taking a nap, the roaring must have been that.
    {name} slowly sneaks up on the dragon, pulling out his newly found sword,
    Then {name} goes for the dragon and successfuly slit its throat.
    {name} discovers that beyond that, in another chamber is a huge pile of treasure.
        CONGRATULATIONS: BEST ENDING ACHIEVED!!
        THE END""")
                
            elif pt5 == "leave":
                points += 4
                print(f"""{name} just decides that this is enough treasure, and just walk out.
    {name} walks to the nearest city, and sell the sword for 10000 dollars,
    as the sword was actually a long lost sword of an ancient king.
    With his new found profits, {name} goes and buys a new house and car.
        THE END""")
                
    elif pt1 == "look":
        points += 1
        print(f"""{name} decides to just sit there and look around
    Waiting...
    Still waiting...
    There seems to be nothing around.
    Do you wish to "leave", or "look" more?""")
        while True:
            pt3 = input(">")
            if pt3 == "leave" or pt3 == "look":
                break
            else:
                print("You must type 'leave' or 'look'.")
                strikes += 1
            if strikes == 5:
                print(f"""{name} took too long to decide, and a dragon came and ate him.
    THE END""")
                return

        if pt3 == "look":
            points += 1
            print(f"""{name} decides to just sit there and continue looking...
    And looking...
    And looking...
    Still nothing...
    Do you wish to "stay", or to "leave"?""")
            while True:
                pt6 = input(">")
                if pt6 == "stay" or pt6 == "leave":
                    break
                else:
                    print("You must type 'stay' or 'leave'.")
                    strikes += 1
                if strikes == 5:
                    print(f"""{name} took too long to decide, and a dragon came and ate him.
    THE END""")
                return
        
            if pt6 == "stay":
                points += 1
                print(f"""{name} decides to just sit there and keep looking still,
    There has to be something...
    Nope...
    Still nothing...
    Then all of a sudden, a dragon comes and swipes {name} up, then eats him!
    THE END""")

            elif pt6 == "leave":
                points += 1
                print(f"""{name} packs up and leaves.
    THE END""")

        elif pt3 == "leave":
            points += 2
            print(f"""{name} decides there is nothing here to further look at, and he leaves.
    {name} finds a village and he decides to spend the night at the inn.
    {name} found a nice room, and he sprawls out onto the bed, and begin to drift into sleep...
    When he wakes up, his arms are bonded, and his mouth covered.
    {name} tries to yell, but it can not get past the bondage.
    {name} sees a guy sharpening a dagger, and then he looks at him, and says:
    "look who's awake" and hands {name} the dagger, and a note, then leaves.
    Does {name} want to "leave" the items behind and leave, or "read" the note?""")

            while True:
                pt7 = input(">")
                if pt7 == "leave" or pt7 == "read":
                    break
                else:
                    print("You must type 'leave' or 'read'.")
                    strikes += 1
                if strikes == 5:
                    print(f"""{name} took too long to decide, and a dragon came and ate him.
    THE END""")
                    return

            if pt7 == "leave":
                points += 1
                print(f"""{name} leaves everything behind and just walk away from the area.
    As he is leaving he is confronted by the guy.
    He says "wrong choice" and kills {name}.
    THE END""")
                
            if pt7 == "read":
                points += 3
                print(f"""{name} decides that he may as well read the note.
    The note states:
    Target: Brandon
    Pay: 1,000,000 dollars
    Deadline: Tomorrow 12 a.m.
    \n{name} wakes up the next day rich.
    THE END""")
    if points == 8:
        print(f"\t\t\tYou scored {points} points! Good job!")
    elif points < 8 and points >4:
        print(f"\t\tYou got {points} points. Maybe try again?")
    else:
        print(f"\tYou got {points} points... Maybe don't make dumb decisions?")
    
if __name__ == "__main__":
    adventure()