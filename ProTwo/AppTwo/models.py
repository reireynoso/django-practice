from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 150, unique=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.last_name