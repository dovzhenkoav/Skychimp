from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


def my_print():
    print('Scheduler works!')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_print, 'interval', minutes=1)
    scheduler.start()
