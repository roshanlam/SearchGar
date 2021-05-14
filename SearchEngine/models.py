from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils import timezone

class SumbitWebsiteModel(models.Model):
    url = models.URLField(max_length=200)
    title = models.TextField(max_length=200)
    def __str__(self):
        return f"{self.title, self.url}"

