from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
