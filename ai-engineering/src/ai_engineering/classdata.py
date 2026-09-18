from dataclasses import dataclass

@dataclass
class ExampleDataClass:
    model:str
    temprature: float
    max_tokens: int =100 #defaults
    
test=ExampleDataClass(model="gpt-4", temprature=0.7)

@dataclass
class EmbeddedConfig:
    model: str ="text-embedding-3-small"
    dimension: int = 1536
    normalize: bool = True
    
test_embedded=EmbeddedConfig()
test_embedded_model=EmbeddedConfig(model ="text-embedding-3-small")
    
print(test_embedded)
print(test_embedded_model)