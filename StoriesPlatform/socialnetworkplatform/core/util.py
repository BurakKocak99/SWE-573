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
    return [getFollower_count(user), getFollowing_count(user)] #first element for Followers second element for Following


def getFollower_count(user):
    return user.following.all().count()

def getFollowing_count(user):
    return User.objects.filter(following=user.id).count()



def get_follower_following_info(requested_user, current_user, is_me):

    following = User.objects.filter(following=requested_user.id)
    followers = requested_user.following.all()

    following_to_list = list()
    followers_to_list = list()


    current_users_following = User.objects.filter(following=current_user.id) # which users current user is following

    for i in following:
        if i.username != current_user.username:
            if i in current_users_following or is_me: ## If the user is the current user than all the users in the following tab should be marked as followed
                following_to_list.append({
                    'username': i.username,
                    'first_name': i.first_name,
                    'last_name': i.last_name,
                    'follow_button': "btn-danger",
                    'follow_text': "Unfollow",
                    'follow_action': "unfollow",
                    'follow_icon': "fa-minus",
                })
            else:
                following_to_list.append({
                    'username': i.username,
                    'first_name': i.first_name,
                    'last_name': i.last_name,
                    'follow_button': "btn-outline-primary",
                    'follow_text': "Follow",
                    'follow_action': "follow",
                    'follow_icon': "fa-plus",
                })

    for j in followers:

        if j.username != current_user.username:
            if j in current_users_following:
                followers_to_list.append({
                    'username': j.username,
                    'first_name': j.first_name,
                    'last_name': j.last_name,
                    'follow_button': "btn-danger",
                    'follow_text': "Unfollow",
                    'follow_action': "unfollow",
                    'follow_icon': "fa-minus",

                })
            else:
                followers_to_list.append({
                    'username': j.username,
                    'first_name': j.first_name,
                    'last_name': j.last_name,
                    'follow_button': "btn-outline-primary",
                    'follow_text': "Follow",
                    'follow_action': "follow",
                    'follow_icon': "fa-plus",

                })




    return following_to_list, followers_to_list


