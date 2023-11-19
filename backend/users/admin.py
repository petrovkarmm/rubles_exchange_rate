from django.contrib import admin

from users.models import TelegramUser, TelegramUserActivity


@admin.register(TelegramUser)
class PostAdmin(admin.ModelAdmin):
    # Отображение полей
    list_display = ['tg_user_id', 'tg_user_first_name', 'tg_user_last_name', 'tg_user_username']
    # Лист фильтрация справа
    list_filter = ['tg_user_registration_time']
    # Строка поиска
    search_fields = ['tg_user_username']
    # Сортировка по стобцам по умолчанию
    ordering = ['tg_user_registration_time']


@admin.register(TelegramUserActivity)
class PostAdmin(admin.ModelAdmin):
    # Отображение полей
    list_display = ['tg_user_id', 'tg_user_username', 'activity_time']
    # Лист фильтрация справа
    list_filter = ['activity_time']
    # Строка поиска
    search_fields = ['tg_user_username']
    # Сортировка по стобцам по умолчанию
    ordering = ['activity_time']