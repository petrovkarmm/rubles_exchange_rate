from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from telegram_commands.models import AiogramCommands


class GetTextForCommand(APIView):
    def get(self, request: Request):
        command = request.data.get('command')

        try:
            command_obj = AiogramCommands.objects.get(command=command)
            result = {
                'text': command_obj.text
            }

            return Response(result, status=status.HTTP_200_OK)

        except:
            result = {
                'text': None
            }

            return Response(result, status=status.HTTP_200_OK)
