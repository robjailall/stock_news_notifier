from config.twilio import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_PHONE_NUM
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = TWILIO_ACCOUNT_SID
# Your Auth Token from twilio.com/console
auth_token = TWILIO_AUTH_TOKEN
from_phone_num = TWILIO_FROM_PHONE_NUM

client = Client(account_sid, auth_token)


def send_message(message, recipient_phone_num):
    message = client.messages.create(
        to=recipient_phone_num,
        from_=from_phone_num,
        body=message)

    print(message.sid)
