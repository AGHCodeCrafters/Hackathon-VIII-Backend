from fastapi import FastAPI, Response, Query
from src.routes.home import home



app = FastAPI()

app.include_router(home.router)
