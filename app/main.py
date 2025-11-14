from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "This is Cloud-DevOps FAT-2"}
