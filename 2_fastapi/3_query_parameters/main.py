from fastapi import FastAPI

app = FastAPI()

dl_models = [
    {"model_1": "Alexnet"},
    {"model_2": "U-net"},
    {"model_3": "Resnet"},
    {"model_4": "CNN"},
    {"model_5": "regression"},
    {"model_6": "logistic"},
]


@app.get("/models/")
async def read_models(skip: int = 0, limit: int = 10):
    return dl_models[skip : skip + limit]


