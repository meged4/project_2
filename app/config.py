from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: int
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    class Config:
        env_file = ".env"


settings = Settings()
settings.DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"