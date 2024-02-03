from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()


@app.get("/students/")
async def read_students(
    first_name: Annotated[str | None, Query(max_length=5, min_length=3)] = None
):
    results = {"student_id": 238754, "surname": "Nicholas"}
    if first_name:
        results.update({"first_name": first_name})
    return results


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=40, le=100)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
