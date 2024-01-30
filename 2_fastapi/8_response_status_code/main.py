"""
Response Status code
YOu can declare the http status code used for the response with the parameter

"""

from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

"""
in http you send a numeric status code of 3 digita as part of the response
100 - information
200 - successful responses(mostly used)
201 - created
204 - no content(used when there is nothing to return to the client)
300 - redirection (no body)
304 - not modified
400 - client error responses
404 - not found
500 - server errors (rarely used directly, when something goes wrong in application code or server, it defaults to this)
"""