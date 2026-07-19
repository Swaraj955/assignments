def count_words():
    filename = input("Enter file name: ")

    file = open(filename, "r")
    data = file.read()
    file.close()

    words = data.split()

    print("Total number of words:", len(words))

count_words()