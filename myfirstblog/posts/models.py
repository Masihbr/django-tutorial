from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)
