from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    avatar = models.ImageField(upload_to="users/", verbose_name="Avatar", null=True, blank=True)

    username = None
    email = models.EmailField(unique=True, verbose_name="Mail")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []