def sum ():
    x = int(input())
    if x > 1 or x < 101 : 
        for a in range(1, x  + 1):
            for b in range(1, x + 1):
                print(a * b, end =" ")
            print()


sum()