from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from account.accountConfig import BlogAccountManager
from django.contrib.auth.models import Group,Permission


class User(AbstractUser):
    username    =models.CharField(max_length=100, unique=True)
    email       = models.EmailField(_("Email"),unique=True)
    date_joined = models.DateTimeField(verbose_name="Date Joined",auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name="Last Login",auto_now_add=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    is_vip = models.BooleanField(default=False) 
    is_active    = models.BooleanField(default=True)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_verified  = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = BlogAccountManager()

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ['-id'] 

    def __str__(self):
        return self.username if self.username else ""

    
