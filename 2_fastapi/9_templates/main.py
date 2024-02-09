from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/students/{student_id}", response_class=HTMLResponse)
async def read_student(request: Request, student_id: str):
    return templates.TemplateResponse(
        request=request, name="students.html", context={"student_id": student_id}
    )


@app.get("/numbers/", response_class=HTMLResponse)
async def get_no(request: Request, no: str = 5):
    return templates.TemplateResponse(
        request=request, name="no.html", context={"no": no}
    )


# pip install Jinja2
