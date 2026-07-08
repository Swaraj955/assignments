def CountDigits(n):
    count = 0

    while n > 0:
        count += 1
        n //= 10

    return count

num = int(input("Enter number: "))
print("Number of digits =", CountDigits(num))