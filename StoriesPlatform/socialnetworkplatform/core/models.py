from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
# This is the first class created according to the UML Class Diagram given in Wiki
# Some of the fields to be added in the future
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name_Surname = models.TextField()
    Username = models.TextField()
    emailaddress = models.EmailField(max_length=40, blank=False, default='email@email.com')
    Password = models.CharField(max_length=15, blank=False, default='password')
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
        return self.title + "\n" + self.story
