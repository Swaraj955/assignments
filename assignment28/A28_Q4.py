def display_file():
    filename = input("Enter file name: ")

    file = open(filename, "r")

    for line in file:
        print(line, end="")

    file.close()

display_file()