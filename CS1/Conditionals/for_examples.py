def count_to(num):
    for i in range(1, num):
        print(i, end=', ')
    print(num, end='.\n')

def count_by(by, num):
    for i in range(by, num+1, by):
        print(i, end=' ')

def countdown(start):
    for i in range(start, 1, -1):
        print(i, end='...')
    print("1...Blastoff!")

def factorial(n):
    val = 1
    for i in range(1, n+1):
        val *= i
        if i < n:
            print(i, end=' * ')
        elif i == n:
            print(f"{n} = {val}")

def div3or7(n):
    val = 0
    for i in range(1, n):
        if i%3 == 0:
            val+=1
        elif i%7 == 0:
            val+=1
    print(f"There are {val} numbers less that {n} that are divisable by 3 or 7.")

#count_to(23)
#count_by(3, 15)
#countdown(10)
#factorial(10)
#div3or7(10)