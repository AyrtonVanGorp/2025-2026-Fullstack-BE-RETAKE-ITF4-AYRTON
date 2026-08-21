import os
from fastapi import FastAPI
from routes.student2_GetEndpoints import router as student2_get_router
from routes.student2_PostEndpoints import router as student2_post_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

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
app.include_router(student2_get_router)
app.include_router(student2_post_router)