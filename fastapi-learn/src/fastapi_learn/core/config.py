from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    llmm_provider:str ="openai"
    model_name:str ="gpt-5"
    model_config=SettingsConfigDict(
        env_file=".env"
    )
    
settings=Settings()