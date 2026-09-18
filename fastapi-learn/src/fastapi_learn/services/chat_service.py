
from fastapi_learn.clients.protocol import LLMClientProtocol 

class ChatService:
    def __init__(self,client:LLMClientProtocol):
        self.client=client
        
    async def generate_response(self,prompt:str)->str:
        return await self.client.generate(prompt)