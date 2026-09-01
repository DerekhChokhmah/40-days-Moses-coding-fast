from fastapi import FastAPI
from schemas import schemaForMonitorAPI
app = FastAPI()


@app.post("/monitors")
async def create_monitor_data(schema: schemaForMonitorAPI):
    details = {
        "name": schema.name,
        "url": schema.url,
        "method": schema.method,
        "expected_status": schema.expected_status,
        "interval_value": schema.interval_value
    }
    return details
