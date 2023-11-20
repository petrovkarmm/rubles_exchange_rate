import os
import asyncio

from aiogram.types import Message

import apsched

from app.routers.main_menu_router import main_menu_router
from app.routers.main_menu_router.keyboards.main_menu_buttons import main_menu_kb
from app.routers.registration_router import registration_router

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, F

from app.routers.registration_router.utils.states import Register

load_dotenv(find_dotenv())


async def cancel_choice(message: Message):
    await message.answer(
        text="Возвращаемся в главное меню.",
        reply_markup=main_menu_kb()
    )


async def main():
    bot = Bot(token='6864910852:AAEYZObmdqfvqXp2zWiijHaxUIhyG3B4gXA')
    dp = Dispatcher()

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(apsched.send_currency_for_subs, trigger='cron',
                      hour=12,
                      minute=0, kwargs={'bot': bot})

    # Тест работы отправки сообщения по подписке.
    # scheduler.add_job(apsched.send_currency_for_subs, trigger='interval', seconds=15, kwargs={'bot': bot})

    scheduler.start()

    dp.include_router(registration_router.router)

    dp.include_router(main_menu_router.router)

    dp.message.register(cancel_choice, Register.end_registration, F.text.lower() == '❌ назад.')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())