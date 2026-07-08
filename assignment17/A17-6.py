def Pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

num = int(input("Enter number: "))
Pattern(num)