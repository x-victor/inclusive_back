from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import BaseModel


class User(BaseModel, AbstractUser):
    middle_name = models.CharField("Отчество", max_length=100, blank=True, default="")
    phone = models.CharField("Телефон", max_length=100, blank=True, default="")
    about = models.TextField("О себе", blank=True, default="")

    class Meta(AbstractUser.Meta):
        ordering = ["-date_joined"]
