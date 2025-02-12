from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

# Dynamic endpoint
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

# Query parameter endpoint
@app.get("/sum")
def calculate_sum(a: int, b: int):
    return {"sum": a + b}

# Request body example
class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/user")
def create_user(user: User):
    return {"message": "User created successfully!", "user": user}

# Dynamic input endpoint
@app.post("/dynamic")
async def dynamic_input(request: Request):
    data = await request.json()
    return {"received_data": data}
