from fastapi import FastAPI, Form, Request,status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from models.user import UserData

app = FastAPI()

templates = Jinja2Templates(directory = "html_templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

userData = []


@app.post('/save_date_of_birth',tags=["Save Data"])
def save_data(data: UserData):
    print(data)
    userData.append(data)
    print(userData)
    return {"user_data": userData}

@app.get('/',tags=["UI"])
async def home(request: Request):
    return templates.TemplateResponse("form.html",{"request": request, "birthdays": userData})

@app.post('/save_form_data/',tags=["Save Data"])
async def save_data_response(name: str = Form(...),month: str = Form(...),day: str = Form(...)):
  
    data = UserData(name = name,month = month,day = day)
    userData.append(data)
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)