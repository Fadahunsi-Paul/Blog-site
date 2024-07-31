from django.db import models
from django.utils import timezone
from account.models import User 
from myblog.basemodel import TimeBaseModel
from django.urls import reverse


class Post(TimeBaseModel):
    author      = models.ForeignKey(User,on_delete=models.CASCADE)
    title       = models.CharField(max_length=100)
    content     = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now )

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})