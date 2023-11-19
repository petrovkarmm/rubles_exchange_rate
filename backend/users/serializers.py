from rest_framework import serializers

from users.models import TelegramUser


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelegramUser
        fields = '__all__'


class UserIDCheckSerializer(serializers.Serializer):
    tg_user_id = serializers.IntegerField()


class UserActivitySerializer(serializers.Serializer):
    tg_user_id = serializers.IntegerField()
    tg_handler_name = serializers.CharField(max_length=45)
    tg_user_username = serializers.CharField(max_length=45)