from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer, UserIDCheckSerializer, UserActivitySerializer
from .models import TelegramUser, TelegramUserActivity


class UserActivity(APIView):
    def get(self, request):
        serializer = UserIDCheckSerializer(data=request.data)

        if serializer.is_valid():
            tg_user_id = serializer.validated_data.get('tg_user_id')

            all_user_activity = (TelegramUserActivity.objects.filter(tg_user_id=tg_user_id)
                                 .values_list('tg_handler_name', 'activity_time')).order_by('-activity_time')

            result = [f'{activity[0]} {activity[1]}' for activity in all_user_activity]

            context = {
                'result': result
            }

            return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserActivitySerializer(data=request.data)

        if serializer.is_valid():
            tg_user_id = serializer.validated_data.get('tg_user_id')
            tg_handler_name = serializer.validated_data.get('tg_handler_name')
            tg_user_username = serializer.validated_data.get('tg_user_username')
            TelegramUserActivity.objects.create(
                tg_user_id=tg_user_id, tg_handler_name=tg_handler_name, tg_user_username=tg_user_username
            )

            context = {
                'result': True
            }

            return Response(context, status=status.HTTP_200_OK)


class UserRegistration(APIView):
    def get(self, request):

        serializer = UserIDCheckSerializer(data=request.data)

        if serializer.is_valid():
            if TelegramUser.objects.filter(
                tg_user_id=serializer.validated_data.get('tg_user_id')
            ).exists():

                context = {
                    'result': False
                }

                return Response(context, status=status.HTTP_400_BAD_REQUEST)

            context = {
                'result': True
            }

            return Response(context, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():

            tg_user_id = serializer.validated_data.get('tg_user_id')

            if TelegramUser.objects.filter(
                tg_user_id=serializer.validated_data.get('tg_user_id')
            ).exists():
                context = {
                    "result": False
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)

            tg_user_first_name = serializer.validated_data.get('tg_user_first_name')
            tg_user_last_name = serializer.validated_data.get('tg_user_last_name')
            tg_user_username = serializer.validated_data.get('tg_user_username')
            tg_user_language = serializer.validated_data.get('tg_user_language')

            TelegramUser.objects.create(
                tg_user_id=tg_user_id, tg_user_first_name=tg_user_first_name, tg_user_last_name=tg_user_last_name,
                tg_user_username=tg_user_username, tg_user_language=tg_user_language
            )

            context = {
                "result": True
            }

            return Response(context, status=status.HTTP_201_CREATED)


class UserSubscribe(APIView):
    def get(self, request):
        serializer = UserIDCheckSerializer(data=request.data)

        if serializer.is_valid():
            tg_user_id = serializer.validated_data.get('tg_user_id')

            try:
                have_a_subscription = TelegramUser.objects.values('have_a_subscription').get(tg_user_id=tg_user_id)

            except:
                have_a_subscription = {
                    'have_a_subscription': False
                }
                return Response(have_a_subscription, status=status.HTTP_200_OK)

            return Response(have_a_subscription, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserIDCheckSerializer(data=request.data)

        if serializer.is_valid():
            tg_user_id = serializer.validated_data.get('tg_user_id')

            user = TelegramUser.objects.get(tg_user_id=tg_user_id)

            if user.have_a_subscription:
                context = {
                    "have_a_subscription": False
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.have_a_subscription = True
                user.save()
                context = {
                    "have_a_subscription": True
                }
                return Response(context, status=status.HTTP_200_OK)


class UserUnSubscribe(APIView):
    def post(self, request):
        serializer = UserIDCheckSerializer(data=request.data)

        if serializer.is_valid():
            tg_user_id = serializer.validated_data.get('tg_user_id')

            user = TelegramUser.objects.get(tg_user_id=tg_user_id)

            if user.have_a_subscription:
                user.have_a_subscription = False
                user.save()
                context = {
                    "unsubscribe": True
                }
                return Response(context, status=status.HTTP_200_OK)
            else:
                context = {
                    "unsubscribe": False
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)


class GettingAllSubs(APIView):
    def get(self, request):
        users_telegram_id = TelegramUser.objects.filter(have_a_subscription=True).values('tg_user_id')
        return Response(users_telegram_id, status=status.HTTP_200_OK)