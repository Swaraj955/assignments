def main():
    filename = input("Enter file name: ")
    word = input("Enter string: ")

    file = open(filename, "r")
    data = file.read()
    file.close()

    count = data.count(word)
    print("Frequency =", count)

main()