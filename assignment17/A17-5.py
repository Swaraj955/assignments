def Prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

num = int(input("Enter number: "))

if Prime(num):
    print("It is Prime Number")
else:
    print("It is Not Prime Number")