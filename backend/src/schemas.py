from pydantic import BaseModel 

class PromptRequest(BaseModel): 
    promp : str


class SchemaResponse(BaseModel):
    result : str
