from fastapi import FastAPI
from models import Response_Error
from analyser import error_analysis
app = FastAPI()


@app.post("/analyze-error")
async def response_error(response:Response_Error):
    return error_analysis(response)

