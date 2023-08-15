from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler

from app_mailing.models import Mailing, MailingTry, Message
from services.email import send_mailing_message


def make_mailing_try(mailing: Mailing):
    message = Message.objects.get(pk=mailing.message.pk)
    title = message.title
    body = message.body
    recipients_list = [recipient.email for recipient in mailing.recipients.all()]
    try:
        send_mailing_message(title, body, recipients_list)
        try_status = 'OK'
        mail_service_response = 'OK'
    except Exception as err:
        try_status = 'Err'
        mail_service_response = err
    finally:
        MailingTry.objects.create(
            mailing=mailing,
            try_datetime=datetime.now(timezone.utc),
            try_status=try_status,
            mail_service_response=mail_service_response
        )


def mailing_schedule():
    active_mailings = Mailing.objects.filter(status='launched')
    for mailing in active_mailings:
        last_mailing_try = MailingTry.objects.filter(mailing=mailing.pk).order_by('-try_datetime')[:1]
        if last_mailing_try:
            last_mailing_try = last_mailing_try.get()
            last_mailing_try_date = last_mailing_try.try_datetime
            time_now = datetime.now(timezone.utc)

            if mailing.periodicity == 'day':
                time_difference = time_now - last_mailing_try_date
                if time_difference.days >= 1:
                    make_mailing_try(mailing)
            elif mailing.periodicity == 'week':
                time_difference = time_now - last_mailing_try_date
                if time_difference.days >= 7:
                    make_mailing_try(mailing)
            else:
                time_difference = time_now - last_mailing_try_date
                if time_difference.days >= 30:
                    make_mailing_try(mailing)
        else:
            pass


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(mailing_schedule, 'interval', seconds=5, id='1')
    scheduler.start()
