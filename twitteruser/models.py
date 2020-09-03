from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    following = models.ManyToManyField(
        "self", symmetrical=False, blank=True)
    display_name = models.CharField(max_length=280)
