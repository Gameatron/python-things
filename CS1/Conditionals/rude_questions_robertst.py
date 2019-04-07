def rude_questions():
    name = input('Hello. what is your name?')
    age = int(input(f'Hi, {name}! How old are you?'))
    print(f"So you're {age}, eh? That's not very old.")
    weight = float(input(f'How much do you weigh, {name}?'))
    print(f"{weight}! Better keep that quiet!!")
    income = float(input(f"What's your income, {name}?"))
    print(f"Hopefully that's ${income} per hour and not per year!")
    phone = input(f'Finally, what kind of phone do you have, {name}?')
    print(f"You have a {phone}! What are you in, the stone age?!?!")
    print(f"Well, thanks for answering my rude questions, {name}.")
    

def main():
    rude_questions()

if __name__ == "__main__":
    main()
    
#on the ones that are expecting a number, if you put words it crashes,
    #is not meant to work with strings or words im asumming.
#if you put numbers for strings they work.

