from django.db import models
from django.contrib.auth.models import AbstractUser


class StartUp(models.Model):

    name_project = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=30)
    short_videos = models.FileField(upload_to="short_videos/")
    description = models.TextField(max_length=500)
    pitchdeck = models.FileField(upload_to="pitchdeck/")


class User(AbstractUser):
    choice_list = models.ManyToManyField(StartUp, through="ChoiceList")


class ChoiceList(models.Model):
    choice_type = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    StartUp = models.ForeignKey(StartUp, on_delete=models.CASCADE)


class PageTinder(models.Model):
    image = models.FileField(upload_to="image/")
    StartUp = models.ForeignKey(StartUp, on_delete=models.CASCADE)
