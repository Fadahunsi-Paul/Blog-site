from django.db import models
from account.models import User
from myblog.basemodel import TimeBaseModel

class Profile(TimeBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    
    