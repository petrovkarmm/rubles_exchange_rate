from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message

from app.data_fetcher import django_user_registration, django_user_check_registration
from app.routers.main_menu_router.keyboards.main_menu_buttons import main_menu_kb
from app.routers.registration_router.keyboards.path_to_registration_button import start_register_kb
from app.routers.registration_router.keyboards.registration_buttons import register_kb

from aiogram.fsm.context import FSMContext
from app.routers.registration_router.utils.states import Register

router = Router()


@router.message(StateFilter(None), Command("start"))
async def cmd_start(message: Message, state: FSMContext):

    data = {
        "tg_user_id": message.from_user.id,
    }

    response = await django_user_check_registration(data=data)

    if response.get('result'):
        await message.answer(
            "Для дальнейшей работы с ботом вам необходимо пройти регистрацию."
            "\nНажав на кнопку Зарегистрироваться вы принимаете условия на обработку данных, а именно: "
            "\nИмя, фамилия, а так же имя пользователя и его ID.",
            reply_markup=register_kb()
        )
        await state.set_state(Register.start_registration)
    else:
        await message.answer(
            'Вы уже были зарегистрированы в системе. Произвожу авторизацию.',
            reply_markup=main_menu_kb()
        )
        await state.set_state(Register.end_registration)


@router.message(StateFilter(None), F.text.lower() == 'начало регистрации')
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        "Для дальнейшей работы с ботом вам необходимо пройти регистрацию."
        "\nНажав на кнопку Зарегистрироваться вы принимаете условия на обработку данных, а именно: "
        "\nИмя, фамилия, а так же имя пользователя и его ID.",
        reply_markup=register_kb()
    )
    await state.set_state(Register.start_registration)


@router.message(Register.start_registration, F.text.lower() == 'зарегистрироваться')
async def end_registration_handler(message: Message, state: FSMContext):

    data = {
        "tg_user_id": message.from_user.id,
        "tg_user_first_name": message.from_user.first_name or None,
        "tg_user_last_name": message.from_user.last_name or None,
        "tg_user_username": message.from_user.username or None,
        "tg_user_language": message.from_user.language_code or None,
    }

    response = await django_user_registration(data)

    if response.get('result'):
        await message.answer(
            "Регистрация прошла успешно.",
            reply_markup=main_menu_kb()
        )

        await state.set_state(Register.end_registration)

    else:
        await message.answer(
            "Вы уже были зарегистрированы в системе. Произвожу авторизацию.",
            reply_markup=main_menu_kb()
        )

        await state.set_state(Register.end_registration)


@router.message(Register.start_registration, F.text.lower() == 'отказ от регистрации')
async def end_registration_handler(message: Message, state: FSMContext):
    await message.answer(
        "Отказ от регистрации. Если вы передумаете, нажмите кнопку ниже.",
        reply_markup=start_register_kb()
    )
    await state.set_state(None)


@router.message(StateFilter(None), F.text)
async def registration_error_handler(message: Message, state: FSMContext):
    data = {
        "tg_user_id": message.from_user.id,
    }

    response = await django_user_check_registration(data)

    if response.get('result'):
        await message.answer(
            "Регистрация не пройдена. Для начала прохождения регистрации нажмите кнопку ниже.",
            reply_markup=start_register_kb()
        )
    else:
        await message.answer(
            "Произвожу повторную авторизацию. Пожалуйста, повторите команду.",
            reply_markup=main_menu_kb()
        )

        await state.set_state(Register.end_registration)
