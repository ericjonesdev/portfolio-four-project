from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.contrib.auth.decorators import login_required


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class UserProfiile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_image = models.ImageField(upload_to="profile/", blank=True)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(help_text='date form:YYYY-MM-DD', blank=True, null=True,)
    location = models.CharField(max_length=50, null=True, blank=True)
    github = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    occupation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def user_profile(request):
        return render("user_profile.html")


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfiile.objects.create(user=instance)
    # Existing users: just save the profile
    try:
        instance.userprofiile.save()
    except UserProfiile.DoesNotExist:
        pass





