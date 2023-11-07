from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from contextlib import asynccontextmanager

#take values from .env file for config var
config = dotenv_values(".env")

app = FastAPI()

#setup lifespan for startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
    #shutdown
    app.mongodb_client.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}