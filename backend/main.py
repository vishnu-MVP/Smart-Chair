#Integration tutorial --part 2

'''from decouple import config
DB_URL = config('DB_URL', cast=str)
DB_NAME = config('DB_NAME', cast=str)'''

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routers.positions import router as pos_router
from fastapi.middleware.cors import CORSMiddleware
origins = [
"http://localhost",
"http://localhost:8080",
"http://localhost:3000",
"http://localhost:8000",
"http://0.0.0.0:10000",
#render links should add -MVP
]

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)


app.include_router(pos_router,prefix='',tags=['pos'])

'''
@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client[DB_NAME]




@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

'''

