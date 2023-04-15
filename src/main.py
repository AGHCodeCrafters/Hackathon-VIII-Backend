from fastapi import FastAPI, Response, Query
from src.routes.home import home
from src.routes.employees import employees


app = FastAPI()

app.include_router(home.router)
app.include_router(employees.router)