from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(max_length=255, null=True)

    avatar = models.ImageField(null=True, default="avatar.png")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
