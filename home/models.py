from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    points = models.IntegerField(default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    upvoted_by = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)

    def upvote(self, user):
        if user in self.upvoted_by.all():
            self.points -= 1
            self.upvoted_by.remove(user)
        else:
            self.points += 1
            self.upvoted_by.add(user)
        self.save()

    def __str__(self):
        return self.title


class HiddenPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    hidden_at = models.DateTimeField(auto_now_add=True)
