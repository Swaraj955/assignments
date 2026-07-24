import schedule
import time

def print_message():
    print("Jay Ganesh...")

schedule.every(2).seconds.do(print_message)

while True:
    schedule.run_pending()
    time.sleep(1)
c