import sys

def main():
    file1 = open(sys.argv[1], "r")
    file2 = open(sys.argv[2], "r")

    if file1.read() == file2.read():
        print("Success")
    else:
        print("Failure")

    file1.close()
    file2.close()

main()