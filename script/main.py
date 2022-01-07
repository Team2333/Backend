from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import DistilBERT_model as ml_model
from minio_client import client

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

# API for Offline pipeline to update model
@app.post("/upload_model_weights/{bucket_name}/{object_name}")
async def load_most_recent_model_weights(bucket_name: str, object_name: str):
    saved_weights_new = client.fetch_update(bucket_name, object_name)
    ml_model.reload(saved_weights_new)
    return {"message": "Successfully loaded the most recent model weights from bucket{} with object name{}".format(bucket_name, object_name)}

# # test API for Offline pipeline to update model
# @app.post("/test_upload_model_weights/{object_name}")
# async def load_most_recent_model_weights(object_name: str):
#     object_name = client.upload(object_name)
#     return {"message": "Successfully loaded {}".format(object_name)}

@app.post("/verify/", response_model=VerificationResult)
async def verify_news(news_content: NewsContent):
    # pass the news_content to the ml model and get the analysed response 
    data, result = ml_model.get_verification_result(news_content.message)
    return {"is_real": result, "data": data}