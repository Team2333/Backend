from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import DistilBERT_model as ml_model

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
class News_Content(BaseModel):
    message: str

# Homepage
@app.get("/")
async def homepage():
    return {"message": "Hello World"}

# TODO: API for Offline pipeline to update model
# @app.post("/upload_model_weights/")
# async def load_most_recent_model_weights(received_file: UploadFile = File(...)):
#     ml_model.reload(received_file.file)
#     return {"message": "Successfully loaded the most recent model weights"}

@app.post("/verify/")
async def verify_news(news_content: News_Content):
    # pass the news_content to the ml model and get the analysed response 
    response = ml_model.get_word_attributions(news_content.message)
    return response