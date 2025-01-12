from pydantic import BaseSettings

class Settings(BaseSettings):
	API_BASE_URL: str = "https://dev.whatcrm.net/v3"
	CURRENCY: str = "RUB"
	CRM: str = "lk"
	TOKEN: str = "5d8af8faaeb61680883a850be0c577e2"

	class Config:
		env_file = ".env"

settings = Settings()