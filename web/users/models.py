import re

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import validate_email
from django.db import models
from rest_framework.exceptions import ValidationError


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create(email, password, **other_fields)

    def create(self, email, password, **other_fields):

        if len(password) < 8 or re.search('([a-zA-z])+(\d)+', password) is None:
            raise ValidationError({'password': 'wrong password'})
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractUser, PermissionsMixin):

    class Roles(models.TextChoices):
        AUTHOR = 'A', 'Author'
        SUBSCRIBER = 'S', 'Subscriber'

    email = models.EmailField(unique=True, validators=[validate_email])
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=1, choices=Roles.choices, default=Roles.SUBSCRIBER)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = None
    username = None
    date_joined = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email
