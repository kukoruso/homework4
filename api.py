from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sum")
def add(number_one: int, number_two: int):
    return {"Number One": number_one, "Number Two": number_two, "Sum": number_one+number_two}