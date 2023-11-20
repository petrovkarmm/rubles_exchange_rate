from django.urls import path

from commands.views import GetTextForCommand

app_name = 'commands'

urlpatterns = [
    path('command-text/', GetTextForCommand.as_view(), name='command-text'),
]
