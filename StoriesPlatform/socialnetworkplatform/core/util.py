from .models import Profile
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()


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


# This function checks if the user1 follows user2: user1 -> user2, user1-> current user

def is_following(user1, user2):
    user2_followers = user2.following.all()
    print()
    if user1 in user2_followers:
        return True
    else:
        return False


# This function checks if the current user is the viewing user or not: currentUser == Viewinguser ?
def isCurrentUser(currentUser, viewingUser):
    if currentUser == viewingUser:
        return True
    else:
        return False


# This function returns a list where first element indicates the number of followers and the second indicates the
# number of following
def getFollowNumbers(user):

    return [getFollower(user), getFollowing(user)] #first element for Followers second element for Following


def getFollower(user):
    return user.following.all().count()

def getFollowing(user):
    return User.objects.filter(following=user.id).count()