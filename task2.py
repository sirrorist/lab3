from fastapi import FastAPI
from pydantic import BaseModel
import requests


class Item(BaseModel):
    text: str


API_URL = (
  "https://api-inference.huggingface.co/models/KoichiYasuoka/bert-base-russian-upos"
)
headers = {"Authorization": "Bearer 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"}


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def query(payload: Item):
    response = requests.post(API_URL, headers=headers, json=payload.text)
    return response.json()
