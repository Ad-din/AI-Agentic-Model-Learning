
from random import randrange
from typing import Optional,List
from fastapi import  FastAPI, HTTPException, Response, status,Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import model
from database import engine,get_db
from sqlalchemy.orm import Session
from routers import posts,users

import schema, util



model.Base.metadata.create_all(bind=engine)



while True:
    try:
        conn=psycopg2.connect(
        host='localhost',
        database='fastapi',
        user='postgres',
        password='admin',
        cursor_factory=RealDictCursor)
        cursor =conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connection to database failed!")
        print("Error:",error)
        time.sleep(2)


app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)


@app.get("/")
def root():
    return{"message":"hello World!!"}