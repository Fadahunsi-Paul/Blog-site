from django.contrib import admin
from blog.models.post import Post
from blog.models.profile import Profile

# Register Models
admin.site.register(Post)
admin.site.register(Profile)