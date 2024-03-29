from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/students/{student_id}", response_class=HTMLResponse)
async def read_student(request: Request, student_id: str):
    return templates.TemplateResponse(
        request=request, name="students.html", context={"student_id": student_id}
    )


# pip install Jinja2
