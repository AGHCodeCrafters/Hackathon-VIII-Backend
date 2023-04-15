from fastapi import FastAPI, Response, Query
from src.routes.home import home
from src.routes.tasks import tasks


app = FastAPI()

app.include_router(home.router)
app.include_router(tasks.router)