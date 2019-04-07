def age_messages():
    name = input(f"Hi, what's your name? ")
    age = float(input(f"Okay, {name}, how old are you? "))
    
    if age < 16:
        message = f"You can't drive, {name}."
    elif age < 18:
        message = f"You can drive, but you can't vote, {name}."
    elif age < 25:
        message = f'You can vote, but not rent a car, {name}.'
    else:
        message = f'You can do pretty much anything, {name}.'
         
    print(f'{message}')
        
def main():
    age_messages()
        

if __name__ == "__main__":
    main()
