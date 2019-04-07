def human_age(age):
    if age < 1:
        term = 'baby'
    if age < 3:
        term = 'toddler'
    elif age < 5:
        term = 'preschooler'
    elif age < 9:
        term = 'child'
    elif age < 13:
        term = 'preteen'
    elif age < 19:
        term = 'teen'
    elif age < 40:
        term = 'young adult'
    elif age < 65:
        term = 'adult'
    else:
        term = 'elderly'
    
    print(f'A human {age} years old is usually called "{term}"')

def main():
    human_age(2.5)
    human_age(4)
    human_age(8.999)
    human_age(18.1)

if __name__ == "__main__":
    main()