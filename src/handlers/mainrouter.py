from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from ..keyboards import (
    get_menu_keyboard, 
    get_category_keyboard,
    get_location_keyboard
)

main_router = Router()

class ChooseState(StatesGroup):
    category = State()
    location = State()

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
async def choose_category(msg: Message, state: FSMContext):
    await msg.answer(
        text="Выберите категорию",
        reply_markup=(await get_category_keyboard()).as_markup()
    )
    await state.set_state(ChooseState.category)

@main_router.callback_query(
    'category' in F.data,
    ChooseState.category
)
async def choose_location(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Выберите локацию для услуг",
        reply_markup=(await get_location_keyboard()).as_markup()
    )
    await state.set_state(ChooseState.location)