from ai_engineering.core.config import settings
from ai_engineering.types_demo import normalize_prompt
from ai_engineering.pydantic import User

test_user = User(id=1, name="John Doe", email="john.doe@example.com")

from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T")

def get_first_item(items: list[T])-> T:
    return items

def main() -> None:
    print(f"AI Engineering project is running! : ({settings.app_name})")
    print(normalize_prompt(prompt=["test","force"]))

# DATA Class equivalent to typescript

@dataclass
class EmbeddedConfig:
    model: str ="text-embedding-3-small"
    dimension: int = 1536
    normalize: bool = True
    
test_embedded=EmbeddedConfig()
test_embedded_model=EmbeddedConfig(model ="text-embedding-3-small")
    
print(test_embedded)
print(test_embedded_model)

if __name__ == "__main__":
    main()