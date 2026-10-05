from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum


class RequestDTO(BaseModel):
    question:str = Field(description="This is the question asked by the user")


class ResponseDTO(BaseModel):
    result:dict = Field(description="This is answer")

app = FastAPI(
    title="My Simple API's",
    description="I am going to deploy these apis on AWS Lambda ?"
)

app.add_middleware(
                   CORSMiddleware, 
                   allow_headers="*", 
                   allow_origins="*", 
                   allow_methods="*"
                   )


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Apis"}


@app.get("/health")
def health():
    return {"status":"OK"}


@app.post("/chat", response_model=ResponseDTO)
def ask(body:RequestDTO):
    return {"result": {"question": body.question, "answer":"This is the response from the ai"}}

handler = Mangum(app, lifespan="off")

