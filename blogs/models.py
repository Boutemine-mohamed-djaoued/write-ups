from django.db import models
from app import settings


class Blog(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    content = models.JSONField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title