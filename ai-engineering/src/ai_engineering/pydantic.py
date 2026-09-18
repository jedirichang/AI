from pydantic import BaseModel, Field

class User(BaseModel):
    prompt:str= Field(default= "This is a prompt", required=True, minimum_length=1, maximum_length=10_000)
    temprature:float= Field(default= 0.7, required=True, ge=0.0, le=1.0)
    max_tokens:int= Field(default= 100, required=True, ge=0, le=10_000)
    model:str= Field(default= "text-embedding-3-small", required=True, minimum_length=1, maximum_length=100)

user= User(prompt="This is a prompt", temprature=0.7, max_tokens=100, model="text-embedding-3-small")
print(user)



