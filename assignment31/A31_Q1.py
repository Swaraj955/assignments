import schedule
import time

message = input("Enter message: ")
interval = int(input("Enter interval in seconds: "))

if interval <= 0:
    print("Interval must be greater than zero.")
else:

    def display_message():
        print(message)

    schedule.every(interval).seconds.do(display_message)

    while True:
        schedule.run_pending()
        time.sleep(1)
