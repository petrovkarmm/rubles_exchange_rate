from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_kb():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='🚀 Старт')
    keyboard_builder.button(text='🌐 Информация о пользователе.')
    keyboard_builder.button(text='💰 Текущий курс рубля.')
    keyboard_builder.button(text='⏳ Помощь')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )