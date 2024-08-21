from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton

from ..config import settings

import aiohttp

async def get_category_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{settings.URL_API}/categories/10") as response:
            buttons = await response.json()
    for button in buttons:
        keyboard.add(KeyboardButton(text=button['name']))
    return keyboard