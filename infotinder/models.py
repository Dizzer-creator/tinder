from django.db import models
from django.contrib.auth.models import AbstractUser


class Startapp(models.Model):

    name_project = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=30)
    short_videos = models.FileField(upload_to="short_videos/")
    description = models.TextField(max_length=500)
    important_image = models.FileField(upload_to="important_image/")
    pitchdeck = models.FileField(upload_to="pitchdeck/")


class User(AbstractUser):
    choice_list = models.ManyToManyField(Startapp, through="Choicelist")


class Choicelist(models.Model):
    choice_type = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startapp = models.ForeignKey(Startapp, on_delete=models.CASCADE)


class Ptinder(models.Model):
    image = models.FileField(upload_to="image/")
    startapp = models.ForeignKey(Startapp, on_delete=models.CASCADE)
