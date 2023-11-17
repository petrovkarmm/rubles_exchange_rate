from django.contrib.auth.models import User
from django.db import models

# 1. ID пользователя (user_id)
# 2. Имя пользователя (first_name)
# 3. Фамилия пользователя (last_name)
# 4. Юзернейм пользователя (username)
# 5. Язык пользователя (language_code)
# 6. Данные о чате, в котором находится пользователь (chat)


class TelegramProfile(models.Model):
    # TODO: add lengths on fields(prob change fields size)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Django Default User')
    tg_user_id = models.IntegerField(verbose_name='User telegram ID')
    tg_user_first_name = models.CharField(verbose_name='User telegram first name')
    tg_user_last_name = models.CharField(verbose_name='User telegram last name')
    tg_user_username = models.CharField(verbose_name='User telegram username')
    tg_user_language = models.CharField(verbose_name='User telegram language')

    def __str__(self):
        return f'{self.tg_user_id, self.tg_user_username}'