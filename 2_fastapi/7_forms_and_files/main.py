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
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


@app.post("/files-to/")
async def create_file(
    file: Annotated[bytes, File()],
    token: Annotated[str, Form()],
    fileb: Annotated[UploadFile, File()] = None,
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
