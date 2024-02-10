from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


# pip install httpx
# pip install pytest
