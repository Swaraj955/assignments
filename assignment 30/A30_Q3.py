import schedule
import time

def print_message():
    print("Coding kar..!")

schedule.every(30).minutes.do(print_message)

while True:
    schedule.run.pending
    time.sleep(1)