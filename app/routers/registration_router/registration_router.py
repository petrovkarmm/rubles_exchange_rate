from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message

from app.routers.main_menu_router.keyboards.main_menu_buttons import main_menu_kb
from app.routers.registration_router.keyboards.path_to_registration_button import start_register_kb
from app.routers.registration_router.keyboards.registration_buttons import register_kb

from aiogram.fsm.context import FSMContext
from app.routers.registration_router.utils.states import Register

router = Router()


@router.message(StateFilter(None), Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    # TODO Добавить запрос к БД о наличии проверки пользователя в БД и переводить в end registration, если есть
    await message.answer(
        "Для дальнейшей работы с ботом вам необходимо пройти регистрацию."
        "\nНажав на кнопку Зарегистрироваться вы принимаете условия на обработку данных, а именно: "
        "\nИмя, фамилия, а так же имя пользователя и его ID.",
        reply_markup=register_kb()
    )
    await state.set_state(Register.start_registration)


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
        await message.answer(
            "Регистрация прошла успешно.",
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
async def registration_error_handler(message: Message):
    await message.answer(
        "Регистрация не пройдена. Для начала прохождения регистрации нажмите кнопку ниже.",
        reply_markup=start_register_kb()
    )