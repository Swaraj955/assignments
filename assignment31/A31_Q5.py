import os
import schedule
import time
from datetime import datetime

directory = input("Enter directory path: ")

def count_files():
    total_files = 0

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            total_files += 1

    filename = "DirectoryCountLog.txt"

    with open(filename, "a") as file:
        file.write("Directory: " + directory + "\n")
        file.write("Number of Files: " + str(total_files) + "\n")
        file.write("Date and Time: " +
                   datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        file.write("-" * 40 + "\n")

    print("Directory:", directory)
    print("Number of Files:", total_files)
    print("Date and Time:",
          datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every(5).minutes.do(count_files)

count_files()

while True:
    schedule.run_pending()
    time.sleep(1)
