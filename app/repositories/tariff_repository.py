from typing import List, Dict
from app.core.http_client import HTTPClient
from app.config.settings import settings
from app.exceptions import ExternalAPIError
from app.logger import logger

class TariffRepository:
	_base_url = f"{settings.API_BASE_URL}/tariffs"
	_headers = {"X-Whatsapp-Token": settings.TOKEN}
	_params = {"currency": settings.CURRENCY, "crm": settings.CRM}

	@classmethod
	async def fetch_all(cls) -> List[Dict]:
		try:
			data = await HTTPClient.get(
				url=cls._base_url,
				headers=cls._headers,
				params=cls._params,
			)
			logger.debug(f"Получены данные: {data}")
			return data
		except Exception as error:
			logger.error(f"Ошибка при получении тарифов: {error}")
			raise ExternalAPIError("Не удалось получить тарифы") from error