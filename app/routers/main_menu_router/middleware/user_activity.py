from typing import Any, Callable, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from app.data_fetcher import django_set_user_activity


class UserActivityMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        telegram_object_dict = dict(event)

        from_user_telegram_object = telegram_object_dict.get('from_user')

        from_user_telegram_object_dict = dict(from_user_telegram_object)

        telegram_user_id = from_user_telegram_object_dict.get('id')
        telegram_user_username = from_user_telegram_object_dict.get('username')
        handler_name = telegram_object_dict.get('text')

        data = {
            "tg_user_id": telegram_user_id,
            "tg_handler_name": handler_name,
            "tg_user_username": telegram_user_username,
        }

        response = await django_set_user_activity(data)

        result = await handler(event, data)

        return result