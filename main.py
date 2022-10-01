from fastapi import FastAPI

server = FastAPI()

@server.get('/')
def welcome():
    return {"Message": "Welcome to my API"}