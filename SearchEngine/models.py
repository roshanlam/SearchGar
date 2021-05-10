from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils import timezone

class SumbitWebsiteModel(models.Model):
    url = models.URLField(max_length=200)
    title = models.TextField(max_length=200)
    def __str__(self):
        return f"{self.title, self.url}"

class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    idd = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('All the users must have an email address')
        user = self.model(email=UserManager.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def update_password(self, idd, current_password, password):
        pass

    def create_admin(self, email, password):
        user = self.create_user(email, password = password)
        user.is_admin = True
        user.save()
        return user

#class Category(models.Model):
#    name = models.CharField(max_length=150)
# TODO: implement Category later
class WebsiteList(models.Model):
    website_name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    added = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
  #  added_at = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
 #   category = models.ForeignKey(Category, default='general')
    class Meta:
        ordering = ['-added'] # order by the added field

    def __str__(self):
        return self.website_name

class Website(models.Model):
    name = models.CharField(max_length=130)
    description = models.CharField(max_length=130)
    
    def __unicode__(self):
        return self.description


class Search(models.Model):
    query = models.TextField()
