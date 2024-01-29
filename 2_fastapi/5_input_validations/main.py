## Query Parameters and String Validations

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

"""
- Explain the | and Union sign

"""


@app.get("/students/")
async def read_students(
    first_name: Annotated[list[str] | None, Query(max_length=50)] = None
):
    results = {"students": [{"student_id": 238754}, {"surname": "Nicholas"}]}
    if first_name:
        results.update({"first_name": first_name})
    return results


"""
- Annotated is for adding meta-data
first_name: Annotated[str | None] = None

- The above means that surname can be a string or none but the default value is optional.
- other validations are max and min length
- to receive multiple values use list[str] in Annotate
"""


@app.get("/fruits/")
async def read_fruits(names: Annotated[list[str] | None, Query()] = None):
    query_fruits = {"names": names}
    return query_fruits


## Path parameters and numeric validations
from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""
Note that path parameters are always required because they are path of a path.
Numeric validations are
- ge
- gt
- le
- lt
"""
