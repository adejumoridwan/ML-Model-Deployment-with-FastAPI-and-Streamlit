from typing import Annotated
from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()


@app.post("/login/")
async def login(
    username: Annotated[str, Form(max_length=5)], password: Annotated[str, Form()]
):
    return {"username": username}


@app.post("/files/")
async def create_file(file: UploadFile):
    return {"filename": file.filename}
