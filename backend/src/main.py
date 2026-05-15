from fastapi import FastAPI 
from schemas import PromptRequest , SchemaResponse

app = FastAPI()

@app.get("/")
def home(): 
    return {"message": "Promp to Schema API is running!"}

@app.post("/api/generate", response_model=SchemaResponse )
async def generate_schema_endpoint(request : PromptRequest):
    user_text = request.requirement
    
@app.get("/health")
def health_check():
    return {"status" : "OK"}


    
    


