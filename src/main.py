from fastapi import FastAPI, Response, Query
from src.routes.home import home
from src.routes.employees import employees
from src.routes.items import items
from src.routes.tasks import tasks
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3001'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(home.router)
app.include_router(employees.router)
app.include_router(items.router)
app.include_router(tasks.router)