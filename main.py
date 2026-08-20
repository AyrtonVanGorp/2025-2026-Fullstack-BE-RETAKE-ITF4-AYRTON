from fastapi import FastAPI
from routes import student1_GETendpoints, student1_POSTendpoints
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello, World!"}



# Both routers can use the same prefix to keep your section organized
app.include_router(student1_GETendpoints.router, prefix="/student1", tags=["Student 1 - Views"])
app.include_router(student1_POSTendpoints.router, prefix="/student1", tags=["Student 1 - Actions"])