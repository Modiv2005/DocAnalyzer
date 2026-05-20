from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Intelligent Document Analytics"
    DATABASE_URL: str = "sqlite:///./doc_analytics.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: int = 8000
    SECRET_KEY: str = "a_very_secret_key_for_jwt_tokens_12345"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1 week

    # AI Providers (can be overridden by environment variables)
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
