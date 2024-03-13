from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.apps import apps


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(username, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=123, blank=True, null=True)
    last_name = models.CharField(max_length=123, blank=True, null=True)
    email = models.EmailField(max_length=123, null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    tel = models.CharField(max_length=123, blank=True, null=True)
    address = models.CharField(max_length=123, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True,)
    project_count = models.IntegerField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    awards = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username
