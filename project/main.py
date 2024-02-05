from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    name: str = Field(default=None, max_length=20)
    sex: str
    age: float = Field(ge=0, description="The age of a student", le=20)
    score: float | None = None


@app.post("/students/{student_id}")
async def update_student(
    student_id: Annotated[int, Path(title="The student id", ge=0, le=100)],
    bmi: float | None = None,
    student: Annotated[Student | None, Body()] = None,
):
    results = {"student_id": student_id}
    if bmi:
        results.update({"bmi": bmi})
    if student:
        results.update({"student": student})
    return results
