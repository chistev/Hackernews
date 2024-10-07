from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    url = models.URLField()  # URL of the post
    points = models.IntegerField(default=1)
    author = models.CharField(max_length=100)  # Author of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    upvoted_by = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)

    def upvote(self, user):
        """Toggles the upvote for the post by a user."""
        if user in self.upvoted_by.all():
            self.points -= 1
            self.upvoted_by.remove(user)
        else:
            self.points += 1
            self.upvoted_by.add(user)
        self.save()

    def __str__(self):
        return self.title
