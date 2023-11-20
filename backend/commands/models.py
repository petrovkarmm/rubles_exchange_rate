from django.db import models


class AiogramCommands(models.Model):
    command = models.CharField(max_length=30)
    text = models.TextField(max_length=150)
