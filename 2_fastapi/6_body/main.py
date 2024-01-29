"""
- You can mix Path, Query and request body parameter freely
- You can also declare body parameters as optional by setting the default to None:
"""

from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    sex: str
    age: float
    score: float | None = None


# starts secondly
class Lecturer(BaseModel):
    name: str
    course: str | None = None


@app.put("/students/{student_id}")
async def update_student(
    student_id: Annotated[int, Path(title="The student id", ge=0, le=1000)],
    bmi: float | None = None,
    student: Student | None = None,
):
    results = {"student_id": student_id}
    if bmi:
        results.update({"bmi": 25.6})
    if student:
        results.update({"student": student})
    return results


@app.put("/lecturers/{lecturer_id}")
async def update_lecturer(lecturer_id: int, student: Student, lecturer: Lecturer):
    results = {
        "lecturer_id": lecturer_id,
        "student": student.model_dump(),
        "lecturer": lecturer.model_dump(),
    }
    return results

#Singular values in body
"""
importance: Annotated[int, Body()]
"""
