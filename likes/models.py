from django.db import models
from app import settings
from blogs.models import Blog

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.user.username} likes {self.blog.title}"
