from pydantic import BaseModel
class Response_Error(BaseModel):
    node: str
    node_type:str
    error:str
    status_code:str

class Error_Analysis(BaseModel):
    root_cause: str
    explanation: str
    evidence: str
    fix: str
    next_action: str