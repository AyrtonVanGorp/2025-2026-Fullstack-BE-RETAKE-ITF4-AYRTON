from fastapi import FastAPI
from routes.student2_get_endpoints import router as student2_get_router
from routes.student2_post_endpoints import router as student2_post_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost",
    "https://localhost",
    "http://127.0.0.1:8080",
    "https://127.0.0.1:8080",
    "https://mysite.netlify.app"
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



# Both routers can use the same prefix to keep your section organized
app.include_router(student1_GETendpoints.router, prefix="/student1", tags=["Student 1 - Views"])
app.include_router(student1_POSTendpoints.router, prefix="/student1", tags=["Student 1 - Actions"])

app.include_router(student2_get_router)
app.include_router(student2_post_router)