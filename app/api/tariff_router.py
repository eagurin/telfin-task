from fastapi import APIRouter, HTTPException
from typing import List
from app.models.tariff import Tariff
from app.services.tariff_service import TariffService
from app.exceptions import ExternalAPIError
from app.logger import logger

router = APIRouter()

@router.get("/tariffs", response_model=List[Tariff])
async def get_tariffs():
	try:
		tariffs = await TariffService.get_tariffs()
		return tariffs
	except ExternalAPIError as error:
		logger.error(f"External API error: {str(error)}")
		raise HTTPException(status_code=502, detail=str(error))
	except Exception as error:
		logger.error(f"Unexpected error in get_tariffs: {str(error)}", exc_info=True)
		raise HTTPException(status_code=500, detail="Internal Server Error")