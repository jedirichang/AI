from fastapi import APIRouter, Depends

from fastapi_learn.dependencies.chat import get_chat_service
from fastapi_learn.services.chat_service import ChatService
router=APIRouter()

@router.get('/chat')
async def chat(
    prompt:str,
    service:ChatService = Depends(get_chat_service)
):
    response= await service.generate_response(prompt)
    
    return {
        "response":response
    }