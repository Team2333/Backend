from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import DistilBERT_model as ml_model
# from minio_client import client

app = FastAPI()

# CORS
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# News to be verified
class NewsContent(BaseModel):
    message: str

class VerificationResult(BaseModel):
    is_real: bool
    data: List = []

# Homepage
@app.get("/")
async def homepage():
    return {"message": "Hello World"}

# TODO: API for Offline pipeline to update model
# @app.post("/upload_model_weights/")
# async def load_most_recent_model_weights(received_file: UploadFile = File(...)):
#     ml_model.reload(received_file.file)
#     return {"message": "Successfully loaded the most recent model weights"}

@app.post("/verify/", response_model=VerificationResult)
async def verify_news(news_content: NewsContent):
    # pass the news_content to the ml model and get the analysed response 
    data, result = ml_model.get_verification_result(news_content.message)
    return {"is_real": result, "data": data}