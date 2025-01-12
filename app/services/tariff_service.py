from typing import List
from app.models.tariff import Tariff
from app.repositories.tariff_repository import TariffRepository
from app.logger import logger
import re

class TariffService:
	@staticmethod
	def _parse_tariff_string(tariff_id: str, tariff_str: str) -> dict:
		# Extract total price using regex
		total_match = re.search(r'Всего: ([\d\s]+[.,]?\d*)₽', tariff_str)
		price = float(total_match.group(1).replace(' ', '').replace(',', '.')) if total_match else 0.0
		
		# Extract name (everything before the dash)
		name = tariff_str.split(' - ')[0].strip()
		
		return {
			'id': int(tariff_id),
			'name': name,
			'price': price,
			'currency': 'RUB',
			'description': tariff_str
		}

	@classmethod
	async def get_tariffs(cls) -> List[Tariff]:
		data = await TariffRepository.fetch_all()
		tariffs = [
			Tariff(**cls._parse_tariff_string(tariff_id, tariff_str))
			for tariff_id, tariff_str in data.items()
		]
		logger.info(f"Обработано {len(tariffs)} тарифов")
		return tariffs