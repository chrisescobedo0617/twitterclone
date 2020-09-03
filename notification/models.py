from django.db import models
from twitteruser.models import MyUser
from tweet.models import Tweet

# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
