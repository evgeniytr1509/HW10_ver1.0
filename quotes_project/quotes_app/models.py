from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)  # User's bio/description
    location = models.CharField(max_length=100, blank=True, null=True)  # User's location
    website = models.URLField(max_length=200, blank=True, null=True)  # User's website or blog URL
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # User's profile picture
    birthdate = models.DateField(blank=True, null=True)  # User's date of birth
    quotes = models.ManyToManyField(Quote, related_name='users_quoted', blank=True)  # User's favorite quotes

    def __str__(self):
        return f'{self.user.username} Profile'