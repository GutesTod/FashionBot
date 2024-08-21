from pydantic_settings import BaseSettings

class SettingsBot(BaseSettings):
    TOKEN: str
    URL_API: str

    class Config:
        env_file = "././.env"
        env_encoding = "utf-8"

settings = SettingsBot()
