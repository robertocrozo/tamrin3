def nth_digit(n):
    big_number = ''.join(map(str, range(1, 5001)))
    
    if 0 < n <= len(big_number):
        print(big_number[n-1])
    else:
        print()

x = int(input())
nth_digit(x)
