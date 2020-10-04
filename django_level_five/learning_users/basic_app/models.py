from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    # Gets user attribute. Basically a model class to add an additional info that the default User does not have
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    # blank means a user can leave it blank
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username