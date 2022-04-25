from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, to_field='email')
    title = models.CharField(max_length=64, null=False)
    content = models.TextField(max_length=1024, null=False)
    public = models.BooleanField(default=True)

