def Reverse(n):
    num = str(n)
    rev= ''.join(reversed(num))
    
    if num == rev:
        print("Yes")
    else:
        print("No")


n = int(input("Enter a number: "))
Reverse(n)
