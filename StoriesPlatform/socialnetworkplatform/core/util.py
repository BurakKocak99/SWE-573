from django.contrib.auth.models import User, auth
from .models import Profile


# This function is for profile creation
def CreateProfile(user):
    profile = Profile()
    user_model = User.objects.get(username=user.username)
    profile.user_id = user_model
    profile.first_name = user_model.first_name
    profile.last_name = user_model.last_name
    profile.Username = user_model.username
    profile.email = user_model.email

    return profile
