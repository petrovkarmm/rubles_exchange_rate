from django.urls import path

from telegram_commands.views import GetTextForCommand

app_name = 'telegram_commands'

urlpatterns = [
    path('command-text/', GetTextForCommand.as_view(), name='command-text'),
]
