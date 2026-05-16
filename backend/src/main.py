from fastapi import FastAPI 
from schemas import PromptRequest , SchemaResponse
from fastapi.responses import HTMLResponse


posts: list[dict] =  [
    {
        "id": 1,
        "author": "John Doe",
        "title": "First post",
        "content": "This is the content of the first post",
        "date_of_posted" : "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe2",
        "title": "Second post",
        "content": "This is the content of the second post",
        "date_of_posted" : "April 21, 2025",
    },
    {
        "id": 3,
        "author": "John Doe3",
        "title": "Third post",
        "content": "This is the content of the third post",
        "date_of_posted" : "April 22, 2025",
    }
]


app = FastAPI()

@app.get("/", response_class=HTMLResponse , include_in_schema=False)
@app.get("/home", response_class=HTMLResponse , include_in_schema=False)
def home(): 
    return f"<h1> {posts[0]['title']}<h1/>"

@app.post("/api/generate", response_model=SchemaResponse )
async def generate_schema_endpoint(request : PromptRequest):
    user_text = request.requirement
    
@app.get("/health")
def health_check():
    return {"status" : "OK"}


    ### from Python FastAPI Tutorial 

@app.get("/api/posts")
def get_posts():
    return posts




    
    


