from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from contextlib import asynccontextmanager

#take values from .env file for config var
config = dotenv_values(".env")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}