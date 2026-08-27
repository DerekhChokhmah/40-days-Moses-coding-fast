import os 
from dotenv import load_dotenv
from openai import OpenAI

from models import Error_Analysis
load_dotenv()
def error_analysis(response):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    ai_response = client.responses.parse(model="gpt-5.6-sol", input="Give the {}, {}, {}, {}, {} for {} {} {} {} ".format("root_cause","explanation","evidence","fix","next_action", response.node, response.node_type, response.error, response.status_code), text_format=Error_Analysis)
    return ai_response.output_parsed
