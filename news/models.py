from django.db import models

from django.contrib.auth.models import User

# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

AUTHOR = (
    (0, "ken"),
    (1, "Wambua"),
    (2, "ken")
)


class dailyhighlights(models.Model):
    # fields of the model
    title = models.CharField(max_length=40, unique=True)

    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.CharField(max_length=10, unique=False)

    updated_on = models.DateTimeField(auto_now=True)

    content = models.TextField()
    img = models.ImageField(upload_to="media")
    created_on = models.DateTimeField(auto_now_add=True)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title


class trendingnews(models.Model):
    # fields of the model
    title = models.CharField(max_length=40, unique=True)

    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.CharField(max_length=10, unique=False)

    updated_on = models.DateTimeField(auto_now=True)

    content = models.TextField()
    img = models.ImageField(upload_to="media")
    created_on = models.DateTimeField(auto_now_add=True)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title



