import schedule
import time
import shutil
from datetime import datetime

source = input("Enter source file path: ")
destination = input("Enter destination folder path: ")

def backup_file():
    backup_name = "backup_" + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".txt"
    destination_file = destination + "/" + backup_name

    shutil.copy(source, destination_file)

    print("Backup completed successfully at",
          datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every().hour.do(backup_file)

while True:
    schedule.run_pending()
    time.sleep(1)
