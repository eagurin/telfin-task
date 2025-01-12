from fastapi import FastAPI, Depends
from services.http_client import HttpClient
from services.tariff_service import TariffService
from typing import Dict, Any

app = FastAPI(title="Tariffs API")

def get_tariff_service() -> TariffService:
	http_client = HttpClient()
	return TariffService(http_client)

@app.get("/tariffs")
async def get_tariffs(
	tariff_service: TariffService = Depends(get_tariff_service),
	currency: str | None = None,
	crm: str | None = None
) -> Dict[str, Any]:
	return await tariff_service.get_tariffs(currency=currency, crm=crm)

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000)