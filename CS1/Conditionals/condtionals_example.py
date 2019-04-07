def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

def age_name(age, name):
    print(f'Hi, my name is {name} and I am {age} years old!')



def main():
    # the code that executes when the program is run
    age_name(15, 'Takoda')
    even_odd(15)
    even_odd(9)
    even_odd(18)
    even_odd(238)
    even_odd(237)
    even_odd(38)
    even_odd(73)
    even_odd(38)
    even_odd(9836742656)
    even_odd(8923623568792364)
    even_odd(24875823472)
    
if __name__ == '__main__':
    main()
    
    