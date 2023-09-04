from twilio.rest import Client

twilio_account_sid = 'AC185c7f8087466629135f91da69479b13'
twilio_auth_token = '4831fec21d29e7972beab0bc99d45ef1'
twilio_phone_number = ' +12295455431'
recipient_phone_number = ' +917989569990'

def send_sms():
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body='Alert ⚠️ ⚠️  Intruder detected',
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print("SMS sent:", message.sid)

