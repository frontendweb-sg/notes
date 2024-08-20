from types import UnionType
from fastapi import FastApi

app = FastApi()


@app.get("/")
def read_root():
    return {"message": "Hello World"}
