from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

from datetime import datetime, timedelta
def get_deadline():
    return datetime.today() + timedelta(days=30)

class Camdo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='camdo')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    product = models.CharField(max_length=30)
    #image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=get_deadline)