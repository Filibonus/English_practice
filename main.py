import uvicorn
from fastapi import FastAPI
from app.api.v1.users import router as users_router

app = FastAPI()

app.include_router(users_router,
                   prefix="/users",
                   tags=["users"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)