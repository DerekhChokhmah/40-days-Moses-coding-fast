from google import genai
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
apikey = os.getenv("API_Sentinel_Alert")
client = genai.Client(api_key=apikey)

interaction = client.interactions.create(model="gemini-3.8-flash", input="Explain how AI works in a few words")
print(interaction.output_text)