def x():
    try:
        x1, y1, x2, y2 = map(int, input().split())
        
        if abs(x1 - x2) == 0:
            print()
        elif abs(y1 - y2) == 0:
            print()
        else:
            print()
    except ValueError:
        print()


x()
