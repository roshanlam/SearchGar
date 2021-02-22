from django.db import models, DatabaseError
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


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

