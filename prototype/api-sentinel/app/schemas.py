from pydantic import BaseModel
class schemaForMonitorAPI(BaseModel):
    name: str
    url: str 
    active: bool
    method: str 
    expected_status: int
    interval_value: int