from typing import List
from app.models.tariff import Tariff
from app.repositories.tariff_repository import TariffRepository
from app.logger import logger

class TariffService:
	@classmethod
	async def get_tariffs(cls) -> List[Tariff]:
		data = await TariffRepository.fetch_all()
		tariffs = [Tariff(**item) for item in data]
		logger.info(f"Обработано {len(tariffs)} тарифов")
		return tariffs