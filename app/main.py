from fastapi import FastAPI
from app.api.tariff_router import router as tariff_router
from app.core.http_client import HTTPClient

app = FastAPI(
	title="Tariff API",
	description="API для получения тарифов",
	version="1.0.0",
)

app.include_router(tariff_router)

@app.on_event("startup")
async def startup_event():
	await HTTPClient.get_session()

@app.on_event("shutdown")
async def shutdown_event():
	await HTTPClient.close_session()