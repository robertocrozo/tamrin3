def mos():
    ag1, ag2, ag3 = map(int, input().split())
    
    if sum([ag1, ag2, ag3]) == 180 and all(angle > 0 for angle in [ag1, ag2, ag3]):
        print("Yes")
    else:
        print("No")

mos()
