from typing import Protocol

class LLMClientProtocol(Protocol):
    def generate(self,prompt:str)->str:
        ...