# WORKING ON #


import threading  # Import the threading module for creating threads
import time
from telethon import TelegramClient

# Your Telegram API credentials
api_id = 'your_api_id'
api_hash = 'your_api_hash'

def drop_telegram_call():
    with TelegramClient('session_name', api_id, api_hash) as client:
        # Find the active call
        dialogs = client.get_dialogs()
        for dialog in dialogs:
            if dialog.is_call:
                # End the ongoing call
                client.disconnect_call(dialog.id)
                print(f"Dropped call in {dialog.title}")

def countdown_and_drop_call():
    # Implement your countdown logic here
    for i in range(3, 0, -1):
        print(f"Countdown: {i}")
        time.sleep(1)  # Wait for 1 second per countdown step

    # After countdown, drop the Telegram call
    drop_telegram_call()

def main():
    # Start a new thread for the countdown and call dropping
    countdown_thread = threading.Thread(target=countdown_and_drop_call)
    countdown_thread.start()

if __name__ == "__main__":
    main()
