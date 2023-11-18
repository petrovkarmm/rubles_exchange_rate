import os
import asyncio

from app.routers.main_menu_router import main_menu_router
from app.routers.registration_router import registration_router


from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher

load_dotenv(find_dotenv())


async def main():
    bot = Bot(token=os.environ.get('AIOGRAM_API_KEY'))
    dp = Dispatcher()

    dp.include_router(registration_router.router)

    dp.include_router(main_menu_router.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())