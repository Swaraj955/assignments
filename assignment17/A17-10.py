def SumDigits(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total

num = int(input("Enter number: "))
print("Sum of digits =", SumDigits(num))