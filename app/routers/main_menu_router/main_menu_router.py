from aiogram import Router, F
from aiogram.types import Message

from app.data_fetcher import (django_get_user_activity,
                              django_get_user_subscribe, django_set_user_subscribe, django_unsubscribe_user)
from app.routers.main_menu_router.keyboards.main_menu_buttons import main_menu_kb, with_subscribe, without_subscribe
from app.routers.registration_router.utils.states import Register

from app.routers.main_menu_router.middleware.user_activity import UserActivityMiddleware

from api.main import CBRApi


router = Router()

router.message.middleware(UserActivityMiddleware())


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


@router.message(Register.end_registration, F.text.lower() == '📖 моя история запросов.')
async def user_activity_handler(message: Message):
    msg = await message.answer(
        "Пожалуйста, подождите немного, пока чат-бот обрабатывает ваш запрос . . ."
    )

    data = {
        "tg_user_id": message.from_user.id,
    }
    response = await django_get_user_activity(data)

    result_string = ''

    for data in response.get('result'):
        result_string += data[:-12] + '\n'

    await msg.delete()

    await message.answer(
        f"{result_string}",
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


@router.message(Register.end_registration, F.text.lower() == '💌 подписка.')
async def subscribe_handler(message: Message):
    data = {
        "tg_user_id": message.from_user.id,
    }

    response = await django_get_user_subscribe(data)

    if response.get('have_a_subscription'):
        await message.answer(
            "Вы подписаны на ежедневную рассылку курса рубля.\n"
            "По желанию вы можете нажать кнопку Отписаться или вернуться в главное меню.",
            reply_markup=with_subscribe()
        )

    else:
        await message.answer(
            "Нажав на кнопку подписаться вы будете получать курс рубля каждый день в 12:00 по Московскому времени.\n"
            "Если вы не готовы к рассылке нажмите Назад.",
            reply_markup=without_subscribe()
        )


@router.message(Register.end_registration, F.text.lower() == '✅ подписаться.')
async def subscribe_user_handler(message: Message):

    data = {
        "tg_user_id": message.from_user.id,
    }

    response = await django_set_user_subscribe(data)

    if response:
        await message.answer(
            "Вы успешно были подписаны на еженедельную рассылку.",
            reply_markup=main_menu_kb()
        )

    else:
        await message.answer(
            "Вы не можете подписаться дважды.",
            reply_markup=with_subscribe()
        )


@router.message(Register.end_registration, F.text.lower() == '⚠️ отписаться.')
async def unsubscribe_user_handler(message: Message):
    data = {
        "tg_user_id": message.from_user.id,
    }

    response = await django_unsubscribe_user(data)

    if response:
        await message.answer(
            "Вы успешно отписались от ежедневного курса рубля.",
            reply_markup=main_menu_kb()
        )

    else:
        await message.answer(
            "Вы не можете отписаться, ведь вы не подписаны.",
            reply_markup=without_subscribe()
        )
