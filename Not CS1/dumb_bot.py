def dumb_bot():
    
    names = ['Takoda']
    pos_ans = ['good','great','fine']
    neg_ans = ['bad', 'terrible', 'awful']
    nei_ans = ["neutral"]
    
    while True:
        name = input("Hi, my name is Brandon, what's yours? ")
        if name in names:
            print(f"Oh, welcome back, {name}")
        
            day = input(f"Hello {name}, how is your day going? ")
            
            #neg_ans.append(word) to make a word learning bot.
            
            if day in pos_ans:
                print('Glad to hear it, mine too!')
            elif day in neg_ans:
                print('Oh that\'s too bad, I\'m not feeling so hot either.')
                input("What seems to be the matter? ")
                print("Oh, I see...")
            else:
                g_or_b = input(f"Oh, is that good or bad, {name}? ")
                if good in g_or_b:
                    pos_ans.append(day)
                    print('Oh, okay.\nGlad to hear it, mine too!')
                elif "bad" in g_or_b:
                    neg_ans.append(day)
                    print('Oh that\'s too bad, I\'m not feeling so hot either.')
                    input("What seems to be the matter? ")
                    print("Oh, I see...")
                if "neither" in g_or_b:
                    nei_ans.append(g_or_b)
                    print("Oh, I see. Fair enough.")
                else:
                    print(f"SYNTAX Error. \"{g_or_b}\" is not recognized.")
            conf = input("Type confirm to restart, or anything to close: ")
            if conf == "confirm":
                pass
            else:
                return
        else:
            names.append(name)
            print(f"Hello, {name}")
            
            day = input(f"So {name}, how are you? ")
            
            #neg_ans.append(word) to make a word learning bot.
            
            if day in pos_ans:
                print('Glad to hear it, mine too!')
            elif day in neg_ans:
                print('Oh that\'s too bad, I\'m not feeling so hot either.')
                input("What seems to be the matter? ")
                print("Oh, I see...")
            else:
                g_or_b = input(f"Oh, is that good or bad, {name}? ")
                if "good" in g_or_b:
                    pos_ans.append(day)
                    print('Oh, okay.\nGlad to hear it, mine too!')
                elif "bad" in g_or_b:
                    neg_ans.append(day)
                    print('Oh that\'s too bad, I\'m not feeling so hot either.')
                    input("What seems to be the matter? ")
                    print("Oh, I see...")
                else:
                    print(f"Well, we will just pretend that is one of my parameters and continue on.")
            conf = input("Type confirm to restart, or anything to close: ")
            if conf == "confirm":
                pass
            else:
                conf = ("Okay buddy try entering an actual parameter.")
                if conf == "confirm":
                    pass
                else:
                    conf = ("Okay buddy try entering an actual parameter.")
                    if conf == "confirm":
                        pass
                    else:
                        conf = ("Okay buddy try entering an actual parameter.")
                        if conf == "confirm":
                            pass
                        else:
                            conf = ("Okay buddy try entering an actual parameter.")
                        if conf == "confirm":
                            pass
                        else:
                            print("Okay I give up. Shutting down now.")
                            return


                        
if __name__ == "__main__":
    dumb_bot()