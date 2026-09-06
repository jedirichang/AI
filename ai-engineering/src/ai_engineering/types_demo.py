from typing import Any
def calculate_token_cost(tokens:int, price_per_token:float)-> float:
    return tokens/price_per_token

def format_prompt(prompt:str, model:str)-> str:
    return f"Model: {model}\n Prompt: {prompt}"

def support(model:str)-> bool:
    return  True if model is 'gpt-5' else False 


#Optional Types
def generate_ai_request(prompt:str, model:str | None = "gpt-5",temperature:float | None= 0.7, system_prompt:str| None =None)-> dict[str,Any]:
    return {"prompt":prompt,"model":model,"temperature":temperature,"system_prompt":system_prompt}

def normalize_prompt(prompt:str | list[str])->str:
    if isinstance(prompt, str):
        return prompt
    return "\n".join(prompt)
    

normalize_prompt("test")