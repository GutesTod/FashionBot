from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

async def get_menu_keyboard() -> ReplyKeyboardBuilder:
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        'Услуги',
        'Регистрация салона'
    ]
    for button in buttons:
        keyboard.add(KeyboardButton(text=button))
    return keyboard