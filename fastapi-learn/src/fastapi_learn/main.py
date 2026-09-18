from fastapi import FastAPI
from typing import Any
from pydantic import BaseModel, Field

from fastapi_learn.api.chat import router


class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1, description="The prompt for the chat model")
    model: str = 'gpt-5'
    
    temperature:float =Field(
        default=0.7,
        ge=0,
        le=2,
    )
    
    max_tokens:int =Field(
        default=1000,
        gt=0
    )
    
class ChatResponse(BaseModel):
    message:str
    response: str
    model:str

app= FastAPI()

app.include_router(router)

@app.get("/")
async def root()-> dict[str, str]:
    return {"message": "AI Engineering API is running"}

@app.get('/models/{model}/info')
async def model_info(model: str) -> dict[str, str]:
    return {"model": model, "status": "available"}

@app.get('/chat/{model}')
async def chat(model:str,temprature:float=0.7,max_tokens:int=1000, streaming:bool=False)-> dict[str, Any]:
    return {"model": model, "temprature": temprature, "max_tokens": max_tokens, "streaming": streaming}

@app.post('/chat')
async def create_chat(request:ChatRequest)->ChatResponse:
    return {"message":"Created chat","response":"Chill","model": request.model}