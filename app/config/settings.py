from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
	API_BASE_URL: str = Field(..., description="Base URL for the WhatsApp API")
	CURRENCY: str = Field(default="RUB", description="Currency for tariffs")
	CRM: str = Field(default="lk", description="CRM system identifier")
	TOKEN: str = Field(..., description="WhatsApp API token")

	class Config:
		env_file = ".env"
		env_file_encoding = "utf-8"
		case_sensitive = True

settings = Settings()