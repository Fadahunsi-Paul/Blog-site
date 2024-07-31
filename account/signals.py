from django.db.models.signals import post_save 
from account.models import User
from django.dispatch import receiver
from blog.models.profile import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_post(sender,instance, **kwargs):
    instance.profile.save()