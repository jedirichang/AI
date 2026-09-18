from fastapi_learn.core.config import Settings

class OpenaiClient:
    def __init__(self,settings:Settings):
        self.settings=settings
        
    async def generate(self,prompt:str)->str:
        return f"Response from {self.settings.model_name}:{prompt}"