from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AiogramCommands


class GetTextForCommand(APIView):
    def get(self, request):
        command = request.data.get('command')

        if AiogramCommands.objects.filter(command=command).first():
            command_obj = AiogramCommands.objects.get(command=command)
            result = {
                'text': command_obj.text
            }
            return Response(result, status=status.HTTP_200_OK)

        result = {
            'text': None
        }
        return Response(result, status=status.HTTP_200_OK)