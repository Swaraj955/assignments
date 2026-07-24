import schedule
import time
from datetime import datetime

def task():
    print("Task executed at:", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every(5).minutes.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
