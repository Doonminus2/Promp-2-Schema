from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home(): 
    return {"message": "Promt to Schema API is running!"}


