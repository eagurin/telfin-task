from typing import Dict, Any
from interfaces.http_client import HttpClientInterface
from config import settings

class TariffService:
	def __init__(self, http_client: HttpClientInterface):
		self._http_client = http_client
		self._base_url = f"{settings.API_URL}/tariffs"

	async def get_tariffs(self, currency: str = settings.DEFAULT_CURRENCY, crm: str = settings.DEFAULT_CRM) -> Dict[str, Any]:
		headers = {"X-Whatsapp-Token": settings.API_TOKEN}
		params = {"currency": currency, "crm": crm}
		return await self._http_client.get(self._base_url, headers=headers, params=params)