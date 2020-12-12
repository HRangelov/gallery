from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='users',
        blank=True
    )
    email = models.CharField(max_length=30, blank=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)




    def __str__(self):
        return self.user.username
