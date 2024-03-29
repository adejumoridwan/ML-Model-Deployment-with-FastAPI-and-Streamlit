## Path Parameters

# you can pass a variable to the path, anything you pass in the path will come out of student_id in the function return value.


from fastapi import FastAPI

app = FastAPI()


@app.get("/students/{student_id}")
async def get_student(student_id):
    return {"student_id": student_id}


## Path parameters with type annotations


from fastapi import FastAPI

app = FastAPI()


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {"student_id": student_id}


- str
- float
- bool

## Order matters


from fastapi import FastAPI

app = FastAPI()

@app.get("/students/3")
async def get_student_3():
    return {"student_id": "student 3"}


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {"student_id": student_id}


## You can't redefine a path operation


from fastapi import FastAPI

app = FastAPI()


@app.get("/students")
async def read_students():
    return ["Tom", "Jerry"]


@app.get("/students")
async def read_students_2():
    return ["Maleek", "Berry"]


## Predefine a value with Enum


from enum import Enum

from fastapi import FastAPI


class StudentName(str, Enum):
    david = "David"
    jonathan = "Jonathan"
    kate = "Kate"


app = FastAPI()


@app.get("/students/{student_name}")
async def get_student(student_name: StudentName):
    if student_name is StudentName.student_name:
        return {"student_name": student_name, "message": "I am a student!"}

    if student_name.value == "Kate":
        return {"student_name": student_name, "message": "I am Kate, I am a lady"}

    return {"student_name": student_name, "message": "We are all students"}


## File path


from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
