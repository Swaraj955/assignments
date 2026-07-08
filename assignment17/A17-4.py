def SumFactors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

num = int(input("Enter number: "))
print("Addition of factors =", SumFactors(num))