from pydantic import BaseModel
from typing import Optional

class Tariff(BaseModel):
	id: int
	name: str
	price: float
	currency: str
	description: Optional[str] = None