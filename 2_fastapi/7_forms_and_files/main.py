# Whenever you want to receive a file instead of JSON you use Form

from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


"""
- the above is requesting for form fields and not JSON
- You can do all the validations and alias you did previously for Query, Path and Cookie
- HTML sends data to a server using form fields
"""

# Request Files
"""
You can define files to be uploaded by the client using File,
because uploaded files are sent as form data
"""

from typing import Annotated

from fastapi import FastAPI, File, UploadFile


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


"""
advantages of Upload file
- you don't have to use File()
- work well for large files like images, videos e.t.c
- you can get the metadata of an uploaded file


"""


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# making upload otional
@app.post("/uploadfiles/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


# Defining Files and Forms together

from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile


@app.post("/files-to/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
