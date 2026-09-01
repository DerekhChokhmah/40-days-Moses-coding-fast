from pydantic import BaseModel
class schemaForMonitorAPI(BaseModel):
    name: str
    url: str 
    method: str 
    expected_status: int
    interval_value: int