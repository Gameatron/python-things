def weight_find():
    earth_weight = float(input("Please enter your Earth weight: "))
    print()
    print("I have info on the following plants")
    print("1. Venus")
    print("2. Mars")
    print("3. Jupiter")
    print("4. Saturn")
    print("5. Uranus")
    print("6. Neptune")
    
    planetno = int(input("Which planet are you visiting? "))
    
    if planetno == 1:
        planet = "Venus"
        planet_g = 0.78
    elif planetno == 2:
        planet = "Mars"
        planet_g = 0.39
    elif planetno == 3:
        planet = "Jupiter"
        planet_g = 2.65
    elif planetno == 4:
        planet = "Saturn"
        planet_g = 1.17
    elif planetno == 5:
        planet = "Uranus"
        planet_g = 1.05
    elif planetno == 6:
        planet = "Neptune"
        planet_g = 1.23
    else:
        print("ERROR: Unknown Planet.")
        return
    
    rel_g = earth_weight * planet_g
    
    print(f'Your weight would be {rel_g} pounds on {planet}')


def main():
    weight_find()

if __name__ == "__main__":
    main()