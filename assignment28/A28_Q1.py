def count_lines():
    filename = input("Enter file name:")

    file = open(filename,"r")
    count = 0

    for line in file:
        count += 1
    
    file.close()

    print("Total number of lines:",count)

count_lines