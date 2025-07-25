from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROYECT_NAME: str = 'Integrados Maquinaria'
    PROYECT_VERSION: str = '0.0.1'
    DATABASE_URL: str 

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()