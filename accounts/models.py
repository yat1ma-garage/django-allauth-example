from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.IntegerField(verbose_name="Age", null=True)
    github_url = models.URLField(verbose_name="GitHub URL", max_length=255, null=True, blank=True)
