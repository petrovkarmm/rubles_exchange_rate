import uuid

from django.contrib.auth.models import User
from django.db import models


class TelegramProfile(models.Model):
    # TODO: add lengths on fields(prob change fields size)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Django Default User')
    tg_user_id = models.IntegerField(verbose_name='User telegram ID')
    tg_user_language = models.CharField(verbose_name='User telegram language')

    def __str__(self):
        return f'{self.tg_user_id, self.user.username}'