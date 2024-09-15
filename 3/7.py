def sum():
    a , b = map(int, input().split())
    
    if not (1 <= a <= 100 and 1 <= b <= 100):
        return
    
    result = sum([a, b])
    print(result)


sum()
