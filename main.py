from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.user import router as user_router


app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user_router)
app.include_router(task_router)


#python -m uvicorn main:app
#uvicorn main:app --reload --port 8001
