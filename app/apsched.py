from aiogram import Bot

from api.main import CBRApi
from app.data_fetcher import django_getting_all_subs


async def send_currency_for_subs(bot: Bot):
    response = await django_getting_all_subs()

    currency_rate_object = CBRApi()
    currency_rate_result = currency_rate_object.get_result

    if currency_rate_result:
        for user_telegram_id in response:
            await bot.send_message(user_telegram_id.get("tg_user_id"),
                                   f'Курс рубля по ежедневной подписке:\n'
                                   f'Курс доллара к рублю: {currency_rate_result.get("USD_RUB")}.\n'
                                   f"Курс евро к рублю: {currency_rate_result.get('EUR_RUB')}.\n"
                                   )
    else:
        for user_telegram_id in response:
            await bot.send_message(user_telegram_id.get("tg_user_id"),
                                   f'На текущий момент присутствуют технические неполадки. '
                                   f'Сегодня рассылки не будет.')