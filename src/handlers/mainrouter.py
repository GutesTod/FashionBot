from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from ..keyboards import get_menu_keyboard

main_router = Router()

@main_router.message(
    Command("start")
)
async def start(msg: Message):
    return msg.answer(
        text="Здравствуйте!", 
        reply_markup=(await get_menu_keyboard()).as_markup(resize_keyboard=True)
    )
@main_router.message(
    F.text == "Услуги"
)
async def choose_category(msg: Message):
    return msg.answer(
        text="Выберите категорию",
        
    )