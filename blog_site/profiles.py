from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


class UserProfiile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile/", blank=True)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    occupation = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
