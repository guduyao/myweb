from django.db import models
from datetime import datetime
# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    addtime = models.DateTimeField(default=datetime.now)