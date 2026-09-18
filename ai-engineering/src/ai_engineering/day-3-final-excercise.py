from dataclasses import dataclass
from typing import Any
from pydantic import BaseModel, Field

@dataclass
class ModelMetadata:
    provider:str
    model_name:str
    supports_streaming: bool = True

class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=1)
    temprature: float = Field(default=0.7, min=0, max=2)
    max_tokens: int = Field(default=1000, gt=0)
    model:str = Field(default="gpt-5")
    
def prepare_generation(
    request: GenerateRequest,
) -> dict[str, Any]:
    return {"prompt": request.prompt, "model": request.model, "max_tokens": request.max_tokens, "temprature": request.temprature}

    
