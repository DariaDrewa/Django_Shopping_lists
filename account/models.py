from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_joined = models.DateTimeField(verbose_name="last_login", auto_now=True)
    # required fields #
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

