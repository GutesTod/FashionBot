from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from ..services import APIClient

async def get_category_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    api_client = APIClient()
    buttons = await api_client.get_categories()
    for button in buttons:
        keyboard.add(InlineKeyboardButton(text=button['name'], callback_data=f"category_{button['name']}"))
    return keyboard