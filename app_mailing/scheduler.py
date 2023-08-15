from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from app_mailing.models import Mailing, MailingTry
from services.email import send_mailing_message


def mailing_schedule():
    active_mailings = Mailing.objects.filter(status='launched')
    print(active_mailings)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(mailing_schedule, 'interval', seconds=5, id='1')
    scheduler.start()
