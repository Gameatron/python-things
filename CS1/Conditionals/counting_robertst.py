def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("BLASTOFF!")
    
def countby(m, n):
    x = m
    while m <= n:
        print(m)
        m += x
        

        
def main():
    countdown(5)
    countby(2, 10)
    
if __name__ == "__main__":
    main()