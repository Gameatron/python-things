def is_divisible(a, b):
    if a%b == 0:
        print(f'{a} is divisible by {b}')

    else:
        print(f'{a} is not divisible by {b}')
    
def main():
    is_divisible(12, 923)
    is_divisible(123822292, 112222)
    is_divisible(23498, 239847)
    is_divisible(293846, 912384)
    is_divisible(8936, 293)
    is_divisible(92384, 203947)
    is_divisible(11, 20)
    is_divisible(6, 9)
    is_divisible(36, 18)
    is_divisible(4, 2)
    

if __name__ == '__main__':
    main()