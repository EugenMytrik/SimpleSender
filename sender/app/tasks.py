from celery import shared_task
from twilio.rest import Client
import os


@shared_task
def send_sms(phone_number):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    twilio_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Your SMS message content", from_=twilio_phone_number, to=phone_number
    )
    print(message.sid)
