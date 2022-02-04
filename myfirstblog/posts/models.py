from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)

    def save(self, *args, **kwargs):
        if not self.title_tag or self.title_tag == "":
            self.title_tag = self.title
        return super(Post, self).save(*args, **kwargs)
