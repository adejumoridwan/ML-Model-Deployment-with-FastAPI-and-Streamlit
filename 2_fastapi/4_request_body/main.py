from fastapi import FastAPI

from pydantic import BaseModel


class Student(BaseModel):
    name: str
    sex: str
    age: int
    height: float | None = None
    weight: float | None = None


app = FastAPI()


@app.post("/students/")
async def create_students(student: Student):
    return student


@app.post("/students/bmi/{student_id}")
async def create_student_bmi(
    student: Student, student_id: str, weight: float, height: float
):
    student_model = student.model_dump()
    if weight and height:
        bmi = weight / height**2
        student_model.update({"bmi": bmi})
    return student_model
