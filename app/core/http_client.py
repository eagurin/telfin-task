import aiohttp
from aiohttp import ClientSession, ClientError
from typing import Optional
from app.logger import logger

class HTTPClient:
	_session: Optional[ClientSession] = None

	@classmethod
	async def get_session(cls) -> ClientSession:
		if cls._session is None or cls._session.closed:
			cls._session = ClientSession()
		return cls._session

	@classmethod
	async def close_session(cls):
		if cls._session and not cls._session.closed:
			await cls._session.close()

	@classmethod
	async def get(cls, url: str, **kwargs):
		try:
			session = await cls.get_session()
			logger.debug(f"Making GET request to {url} with params: {kwargs.get('params', {})} and headers: {kwargs.get('headers', {})}")
			async with session.get(url, **kwargs) as response:
				logger.debug(f"Response status: {response.status}")
				if response.status >= 400:
					error_body = await response.text()
					logger.error(f"Error response body: {error_body}")
				response.raise_for_status()
				data = await response.json()
				logger.info(f"GET {url} - Status {response.status}")
				return data

		except ClientError as e:
			logger.error(f"HTTP client error for {url}: {str(e)}")
			raise
		except Exception as e:
			logger.error(f"Unexpected error during HTTP request to {url}: {str(e)}")
			raise