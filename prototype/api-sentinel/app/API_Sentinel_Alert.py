from google import genai
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
apikey = os.getenv("API_Sentinel_Alert")
client = genai.Client(api_key=apikey)
def response_monitoring_alert(prompt):
  interaction = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
  return interaction.text