from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from ..services import APIClient

async def get_location_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    api_client = APIClient()
    buttons = await api_client.get_locations()
    for button in buttons:
        keyboard.add(InlineKeyboardButton(text=button['name'], callback_data=f"location_{button['name']}"))
    return keyboard