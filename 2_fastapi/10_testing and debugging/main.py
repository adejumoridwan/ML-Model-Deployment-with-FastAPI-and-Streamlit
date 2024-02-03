"""
- you can install httpx using 
- pip install httpx
- You can use the TestClient to create tests functions that start with "test_"
which is the standard pytest conventions
"""
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
