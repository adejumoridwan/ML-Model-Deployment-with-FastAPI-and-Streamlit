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
async def create_student(student: Student):
    return student


@app.post("/students/bmi/")
async def create_student_bmi(student: Student):
    student_model = student.model_dump()
    if student.height and student.weight:
        bmi = student.weight / student.height**2
        student_model.update({"bmi": bmi})
    return student_model
