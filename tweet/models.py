from django.db import models
from twitteruser.models import MyUser
from django.utils import timezone

# Create your models here.


class Tweet(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)
    text = models.TextField(max_length=140)
