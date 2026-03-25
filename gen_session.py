"""
Run this ONCE locally:
  python3 gen_session.py

Enter your phone number and the OTP Telegram sends you.
It will print a SESSION_STRING — copy it and add it to Railway Variables.
"""
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID   = 31030384
API_HASH = "35b04ff5fb54744d4439f3d1c41e4230"

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("\n\n========== COPY THIS ENTIRE STRING ==========")
    print(client.session.save())
    print("=============================================\n")
