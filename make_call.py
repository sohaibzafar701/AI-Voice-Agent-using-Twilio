import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
ngrok_url = os.getenv("NGROK_URL")
from_phone = os.getenv("TWILIO_PHONE_NUMBER")
to_phone = "+923225482701"  # Replace with a valid phone number

client = Client(account_sid, auth_token)

try:
    call = client.calls.create(
        url=f"{ngrok_url}/outgoing-call",
        to=to_phone,
        from_=from_phone
    )
    print(f"Call initiated with SID: {call.sid}")
except Exception as e:
    print(f"Error initiating call: {e}")