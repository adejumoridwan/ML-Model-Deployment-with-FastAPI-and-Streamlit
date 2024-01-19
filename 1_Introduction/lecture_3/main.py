from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "Student"}

@app.get("/bro")
def page():
    return {"Hi": "Bro"}
