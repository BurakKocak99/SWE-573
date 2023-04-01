from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
#This is the first class created according to the UML Class Diagram given in Wiki
# Some of the fileds to be added in the future
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    Name = models.TextField()
    Surname = models.TextField()
    Username = models.TextField()
    Password = models.TextField()
    #Stories to be created
    #Followers to be created

    def __str__(self):
        return self.Username