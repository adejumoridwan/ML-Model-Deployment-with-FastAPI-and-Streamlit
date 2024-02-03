from typing import Annotated

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel


fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

app = FastAPI()


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item
    return item
