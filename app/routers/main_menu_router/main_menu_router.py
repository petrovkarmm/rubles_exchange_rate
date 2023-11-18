from contextlib import suppress

from aiogram import Router, F
from aiogram.types import Message

from app.routers.main_menu_router.keyboards.main_menu_buttons import main_menu_kb
from app.routers.registration_router.utils.states import Register

from aiogram.methods.delete_message import DeleteMessage

from api.main import CBRApi


router = Router()


@router.message(Register.end_registration, F.text.lower() == '🌐 информация о пользователе.')
async def about_user_handler(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    user_language_code = message.from_user.language_code

    await message.reply(
        f"Выдаю информацию о Вас.\n"
        f"ID пользователя: {user_id}.\n"
        f"Имя: {first_name}.\n"
        f"Фамилия: {last_name}.\n"
        f"Юзернейм: {username}.\n"
        f"Текущий язык телеграмма: {user_language_code}.",
        reply_markup=main_menu_kb()
    )


@router.message(Register.end_registration, F.text.lower() == '💰 текущий курс рубля.')
async def rub_currency_rate_handler(message: Message):
    msg = await message.answer(
        "Пожалуйста, подождите немного, пока чат-бот обрабатывает ваш запрос . . ."
    )

    currency_rate_object = CBRApi()
    currency_rate_result = currency_rate_object.get_result

    if currency_rate_result:
        await msg.delete()
        await message.reply(
            f"Выдаю информацию о текущем курсе рубля.\n"
            f"Курс доллара к рублю: {currency_rate_result.get('USD_RUB')}.\n"
            f"Курс евро к рублю: {currency_rate_result.get('EUR_RUB')}.\n",
            reply_markup=main_menu_kb()
        )

    else:
        await message.answer(
            "На текущий момент присутствуют технические неполадки.\n"
            "Пожалуйста, повторите попытку позже.",
            reply_markup=main_menu_kb()
        )
