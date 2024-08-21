from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from typing import Callable, Dict, Awaitable, Any

class LoggerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        result = await handler(event, data)
        
        print(event)
        return result