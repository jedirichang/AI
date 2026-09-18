from pydantic import BaseModel,Field
class ChatRequest(BaseModel):
    prompt: str = Field(..., description="The prompt for the chat request")
    model:str =Field(..., default="gpt-3.5-turbo", description="The model to use for the chat request")
    temperature:float=Field(..., min=0.0, max=2.0, description="The temperature for the chat request")
    
class ResponseModel(BaseModel):
    response: str = Field(..., description="The response from the chat model")
    provider: str = Field(..., description="The provider of the chat model response")
    model: str = Field(..., description="The model used for the chat model response")