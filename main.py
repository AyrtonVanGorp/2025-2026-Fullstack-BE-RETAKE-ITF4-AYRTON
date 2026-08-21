import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.student2_GetEndpoints import router as student2_get_router
from routes.student2_PostEndpoints import router as student2_post_router

app = FastAPI()

origins = [
    "https://splendid-toffee-b8c470.netlify.app",
    "http://localhost:63343",
    "http://localhost",
    "https://localhost",
    "http://127.0.0.1:8080",
    "https://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def main():
    return {"message": "Hello, World!"}


app.include_router(student2_get_router)
app.include_router(student2_post_router)