import httpx , os
from dotenv import load_dotenv

load_dotenv()
webhook_slack = os.getenv("SLACK_WEBHOOK_URL")
def slack_notif_sender(message):
 if not webhook_slack:
    raise ValueError("SLACK_WEBHOOK_URL is missing from .env")
 slack_message = {"text": message}
 response = httpx.post(webhook_slack, json=slack_message)
 response.raise_for_status()

