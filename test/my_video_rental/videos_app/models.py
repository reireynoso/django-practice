from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=256, unique=False)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Customer(models.Model):
    first_name = models.CharField(max_length=256, unique=False)
    last_name = models.CharField(max_length=256, unique=False)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name