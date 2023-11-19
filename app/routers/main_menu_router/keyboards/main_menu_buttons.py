from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_kb():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='🌐 Информация о пользователе.')
    keyboard_builder.button(text='💰 Текущий курс рубля.')
    keyboard_builder.button(text='💌 Подписка.')
    keyboard_builder.button(text='📖 Моя история запросов.')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )


def with_subscribe():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='⚠️ Отписаться.')
    keyboard_builder.button(text='❌ Назад.')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )


def without_subscribe():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='✅ Подписаться.')
    keyboard_builder.button(text='❌ Назад.')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )