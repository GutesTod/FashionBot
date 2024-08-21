from aiogram import Bot, Dispatcher

import asyncio
from asyncio.log import logger

from src.config import settings
from src.middleware import LoggerMiddleware
from src.handlers import main_router

import logging

bot = Bot(token=settings.TOKEN)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    dp = Dispatcher()

    try:
        dp.message.middleware(LoggerMiddleware())
        dp.callback_query.middleware(LoggerMiddleware())
        dp.include_routers(
            main_router
        )
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.get_session()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")