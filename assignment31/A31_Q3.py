import os
import schedule
import time
from datetime import datetime

directory = input("Enter directory path: ")

def scan_directory():
    files = 0
    folders = 0

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            files += 1
        elif os.path.isdir(path):
            folders += 1

    print("\nDirectory Scanned:", directory)
    print("Total Files:", files)
    print("Total Subdirectories:", folders)
    print("Scan Time:", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every(1).minutes.do(scan_directory)

scan_directory()

while True:
    schedule.run_pending()
    time.sleep(1)
