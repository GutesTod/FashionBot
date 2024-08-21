import asyncio
import aiohttp

from src.config import settings

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{settings.URL_API}/categories/10") as response:
            buttons = await response.json()
    print(buttons.values())

if __name__ == '__main__':
    asyncio.run(main())