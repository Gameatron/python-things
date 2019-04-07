def is_divisable(a, b):
    if a%b > 0:
        print(f'{a} is divisable by {b}')

    else:
        print(f'{a} is not divisable by {b}')
    
def main():
    a = float(input('Please select a number: '))
    b = float(input('Please select another number: '))
    is_divisable(a, b)
    
    

if __name__ == '__main__':
    main()