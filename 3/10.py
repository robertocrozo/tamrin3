def count_and_sum_divisors(n):
    all = 0
    jam = 0
    
    for i in range (1, n + 1):
        divisors = [j for j in range(1, i + 1) if i % j == 0]
        all += len(divisors)
        jam += sum(divisors)
    
    print(all, jam)


n = int(input("Enter a number: "))
count_and_sum_divisors(n)
