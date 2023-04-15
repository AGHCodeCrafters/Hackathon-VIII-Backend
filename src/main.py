from fastapi import FastAPI, Response, Query
from src.routes.home import home
from src.routes.employees import employees
from src.routes.items import items
from src.routes.tasks import tasks




app = FastAPI()

app.include_router(home.router)
app.include_router(employees.router)
app.include_router(items.router)
app.include_router(tasks.router)