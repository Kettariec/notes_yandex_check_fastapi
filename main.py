from fastapi import FastAPI
from users.router import router as router_user
from notes.router import router as notes_router

app = FastAPI()

app.include_router(router_user)
app.include_router(notes_router)
