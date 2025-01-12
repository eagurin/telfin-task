import aiohttp
from typing import Dict, Any
from interfaces.http_client import HttpClientInterface

class HttpClient(HttpClientInterface):
	async def get(self, url: str, headers: Dict[str, str], params: Dict[str, str]) -> Dict[str, Any]:
		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				response.raise_for_status()
				return await response.json()