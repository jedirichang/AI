from ai_engineering.core.config import settings
from ai_engineering.types_demo import normalize_prompt
def main() -> None:
    print(f"AI Engineering project is running! : ({settings.app_name})")
    print(normalize_prompt(prompt=["test","force"]))


if __name__ == "__main__":
    main()