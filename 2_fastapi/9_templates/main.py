"""
- These are file structures that are used to represent the application 
user interface, they are separated from the application logic.
- You can use the Jinja2Templates or any other templating engine of you choice.
- Install using pip install jinja2
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

"""
Mounting means the application mounted is independent of the fast api application and will not reflect on the fastapi docs
"""
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/students/{student_id}", response_class=HTMLResponse)
async def read_item(request: Request, student_id: str):
    return templates.TemplateResponse(
        request=request, name="students.html", context={"student_id": student_id}
    )
