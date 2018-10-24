from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class MyFoodManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(username=username,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self.db)
        return user


class MyFoodUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30,
                                validators=[
                                    RegexValidator(regex=USERNAME_REGEX,
                                                   message='Username mustbe alphanumeric or contain numbers',
                                                   code='invalide_username')],
                                unique=True)
    email = models.EmailField(unique=True,
                              verbose_name='email_address')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyFoodManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

