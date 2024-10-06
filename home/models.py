from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    url = models.URLField()  # URL of the post
    points = models.IntegerField(default=1)
    author = models.CharField(max_length=100)  # Author of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return self.title
