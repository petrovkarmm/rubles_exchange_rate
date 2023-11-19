from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class TelegramUser(models.Model):
    # TODO add length on model
    tg_user_id = models.IntegerField(primary_key=True)
    tg_user_first_name = models.CharField(max_length=30, blank=True, null=True)
    tg_user_last_name = models.CharField(max_length=30, blank=True, null=True)
    tg_user_username = models.CharField(max_length=30, blank=True, null=True)
    tg_user_language = models.CharField(max_length=5, blank=True, null=True)
    tg_user_registration_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    have_a_subscription = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tg_user_id, self.tg_user_username, self.have_a_subscription}'


class TelegramUserActivity(models.Model):
    tg_user_id = models.IntegerField()
    tg_user_username = models.CharField(max_length=30, blank=True, null=True)
    tg_handler_name = models.CharField(max_length=60, verbose_name='Название активности в telegram')
    activity_time = models.DateTimeField(auto_now_add=True, verbose_name='Время актиновсти в telegram')

    def __str__(self):
        return f'{self.tg_user_username}, {self.activity_time}'


# Функция-обработчик для сигнала pre_save
# Если количество записей пользователя больше 15, удаляет самую старую по дате и добавляет новую.
@receiver(pre_save, sender=TelegramUserActivity)
def update_activity_time(sender, instance, **kwargs):
    if TelegramUserActivity.objects.filter(tg_user_id=instance.tg_user_id).count() >= 15:
        oldest_activity = (TelegramUserActivity.objects.filter(tg_user_id=instance.tg_user_id)
                           .order_by('activity_time')
                           .first())
        oldest_activity.delete()