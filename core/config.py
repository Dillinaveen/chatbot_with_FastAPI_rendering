from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Secure FastAPI Chatbot"
    VERSION: str = "2.0.0"
    
    MODEL_NAME: str = "facebook/blenderbot-400M-distill"
    
    SECRET_KEY: str  
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()


