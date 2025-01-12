from pydantic_settings import BaseSettings

class Settings(BaseSettings):
	API_URL: str = "https://dev.whatcrm.net/v3"
	API_TOKEN: str = "5d8af8faaeb61680883a850be0c577e2"
	DEFAULT_CURRENCY: str = "RUB"
	DEFAULT_CRM: str = "lk"

settings = Settings()