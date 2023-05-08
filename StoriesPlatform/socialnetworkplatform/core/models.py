from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    following = models.ManyToManyField(  # who is following this user
        "self", blank=True, symmetrical=False
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


User = get_user_model()


# Create your models here.
# This is the first class created according to the UML Class Diagram given in Wiki
class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    Username = models.CharField(default=0, max_length=200)
    email = models.EmailField(max_length=100, blank=False)
    Biography = models.TextField()

    def __str__(self):
        return self.Username


class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    story = models.TextField()
    time = models.DateField()
    placeID = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    to_Story = models.ForeignKey(Story, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.comment


class Likes(models.Model):
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    to_Story = models.ForeignKey(Story, on_delete=models.CASCADE)

    def __str__(self):
        return self.liked_by.username + " liked the story: " + self.to_Story.title
