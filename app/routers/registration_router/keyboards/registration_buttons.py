from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def register_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Зарегистрироваться")
    kb.button(text="Отказ от регистрации")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)