import schedule
import time

def monday_message():
    print("Start your weekly goals")

def wednesday_message():
    print("Review your weekly progress")

def friday_message():
    print("Weekly work completed")

schedule.every().monday.at("09:00").do(monday_message)
schedule.every().wednesday.at("17:00").do(wednesday_message)
schedule.every().friday.at("18:00").do(friday_message)

while True:
    schedule.run_pending()
    time.sleep(1)
