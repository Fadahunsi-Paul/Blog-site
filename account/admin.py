from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["email"]

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)