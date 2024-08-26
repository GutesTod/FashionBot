import aiohttp
from ..config import settings

class APIClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(APIClient, cls).__new__(cls, *args, **kwargs)
            cls._instance.session = aiohttp.ClientSession()
        return cls._instance

    async def get_locations(self):
        url = f"{settings.URL_API}/services/enum"
        async with self._instance.session.get(url) as response:
            return await response.json()
    
    async def get_categories(self):
        url = f"{settings.URL_API}/categories/10"
        async with self._instance.session.get(url) as response:
            return await response.json()

    async def get_services(self, category):
        url = f"{settings.URL_API}/services/{category}"
        async with self._instance.session.get(url) as response:
            return await response.json()

    async def close(self):
        await self._instance.session.close()