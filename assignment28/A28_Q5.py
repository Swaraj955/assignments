def search_word():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    file = open(filename, "r")
    data = file.read()
    file.close()

    if word in data:
        print(word, "is found in the file.")
    else:
        print(word, "is not found in the file.")

search_word()