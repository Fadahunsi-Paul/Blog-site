from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class BlogAccountManager(BaseUserManager):
    def create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError(_("Email must be provided"))
        if not "@" not in email or ".com" not in email:
            raise ValueError(_("Email must have @ and .com ")) 
        if len(password)<8:
            raise ValueError(_("Password must have at least 8 characters")) 
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password) 
        user.save() 
        return user

    def create_superuser(self,email,password, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_admin",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must contain is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must contain is_superuser=True."))
        if extra_fields.get("is_admin") is not True:
            raise ValueError(_("Superuser must contain is_admin=True."))
        return self.create_user(email,password, **extra_fields)
        

