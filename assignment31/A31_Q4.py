import schedule
import time
from datetime import datetime

def create_log():
    filename = "log_" + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".txt"

    with open(filename, "w") as file:
        file.write("Log File Created\n")
        file.write("Creation Time: " +
                   datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

    print("Log file created successfully.")
    print("Creation Time:",
          datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every(10).minutes.do(create_log)

create_log()

while True:
    schedule.run_pending()
    time.sleep(1)
