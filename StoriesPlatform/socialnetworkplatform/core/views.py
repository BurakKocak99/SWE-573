import json
from django.shortcuts import render, redirect, resolve_url
from django.http import JsonResponse, HttpResponseBadRequest
from .forms import RegistrationForm, PostForm, EditProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile, Story, Comment, Likes
from .util import CreateProfile, isCurrentUser, is_following, getFollowNumbers, getFollower_count, getFollowing_count, \
    get_follower_following_info, getLikeCount, getComments, createComment, validateComment, checkLiked, \
    get_story_details, get_story_list, stories_to_list
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

User = get_user_model()


# Create your views here.

@login_required(login_url="/login")
def home(request):
    stories = get_story_list(request.user.id)

    context = {
        'stories': get_story_details(stories),
    }
    return render(request, 'home.html', context=context)


# This function is for signup
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            CreateProfile(user).save()
            login(request, user)
            # Add profileCreation
            return redirect('home')
        else:
            print("Form is not valid!")
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form})


@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            return redirect('home')
        else:
            print("Post Form was not valid!!!")
    else:
        form = PostForm()

    return render(request, 'Post/create_post.html', {"form": form})


@login_required(login_url='/login')
def edit_profile(request):
    profile = Profile.objects.get(Username=request.user.username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user_id = profile.user_id
            new_profile.id = profile.id
            new_profile.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'profile/edit_profile.html', {"form": form})


@login_required(login_url='/login')
def viewprofile(request, slug):
    requested_user = User.objects.get(username=slug)
    stories = Story.objects.all().filter(author_id=requested_user)
    is_me = isCurrentUser(request.user.username, slug)
    following = is_following(request.user, requested_user)
    follow_context = getFollowNumbers(requested_user)
    about_me = Profile.objects.get(user_id=requested_user).Biography
    context = {
        'stories': get_story_details(stories),
        'username': slug,
        'is_me': is_me,
        'follower': follow_context[0],
        'following': follow_context[1],
        'about_me': about_me,

    }
    if not is_me:
        if not following:
            context.update({
                'follow_text': "Follow",
                'follow_action': "follow",
                'follow_icon': "fa-plus",
                'follow_button': "btn-info",
            })
        else:
            context.update({
                'follow_text': "Unfollow",
                'follow_action': "unfollow",
                'follow_icon': "fa-minus",
                'follow_button': "btn-danger"
            })

    return render(request, 'profile/view_profile.html', context=context)


class FollowToggle(LoginRequiredMixin, View):
    """
    This Class handles all of the follow/unfollow operations along with error handling.
    It returns Json data which represents the current state of the following for currentUser -> requestedUser
    Params:
        data
        {
            action: action requested -> follow/unfollow
            username: the username of the user which current user wants to follow/unfollow
            ... more to be added if needed
        }
    Returns:
          JsonResponse
          {
            done: successful or not
            wording: Wording for buttons used for follow/unfollow actions
            action: to change the state of the action on html page in button class
            follower: to dynamically change the number of followers in HTML
            ... more to be added if needed
          }
    """

    @staticmethod
    def post(request, *args, **kwargs):
        data = request.POST.dict()
        # Check if the necessary fields exists in the data if not return Bad Request
        if "action" not in data or "username" not in data and request.user.username != data['username']:
            return HttpResponseBadRequest("Action and Username must be present!")

        current_user = request.user
        try:
            requested_user = User.objects.get(username=data['username'])
        except ValueError:
            return HttpResponseBadRequest("Could not find the user requested!")
        following_users = requested_user.following.all()
        # If current user wants to follow another user. CurrentUser -> request.user, OtherUser-> data['username']
        if data['action'] == 'follow':

            if current_user in following_users:  # Action is follow but uer is already following resync the Front End
                return JsonResponse({
                    'done': False,
                    'wording': "Unfollow",
                    'action': 'unfollow',
                })
            requested_user.following.add(current_user.id)


        # If current user wants to unfollow another user
        elif data['action'] == 'unfollow':
            if current_user not in following_users:  # Action is follow but uer is already following resync the Front End
                return JsonResponse({
                    'done': False,
                    'wording': "Follow",
                    'action': 'follow',
                })
            requested_user.following.remove(current_user.id)

        return JsonResponse(
            {
                'done': True,
                'wording': "Unfollow" if data['action'] == "follow" else "Follow",
                'action': 'unfollow' if data['action'] == "follow" else "follow",
                'follower': getFollower_count(requested_user)
            }
        )


def follower_page(request, slug):
    requested_user = User.objects.get(username=slug)
    follow_context = getFollowNumbers(requested_user)
    is_me = isCurrentUser(request.user.username, slug)
    following_list, follower_list = get_follower_following_info(requested_user, request.user, is_me)
    print(follower_list)
    context = {
        'follower_number': follow_context[0],
        'following_number': follow_context[1],
        'follower_list': follower_list,
        'following_list': following_list,
        'viewed_user': requested_user,
    }

    return render(request, 'profile/follower.html', context=context)


@login_required(login_url='/login')
def viewPost(request, story_id):
    story = Story.objects.get(id=story_id)
    like_count = getLikeCount(story)
    comments = getComments(story)
    is_liked = checkLiked(story, request.user)
    context = {
        'story_id': story.id,
        'placeId': story.placeID,
        'comments': comments,
        'viewed_user': story.author,
        'story_title': story.title,
        'story': story.story,
        'likes': like_count,
        'story_time': story.created_at,
        'like_btn': "fa-solid" if is_liked else "fa-regular",
    }

    return render(request, 'post/viewpost.html', context=context)


class LikeToggle(LoginRequiredMixin, View):
    @staticmethod
    def post(request, *args, **kwargs):
        data = request.POST.dict()
        story = Story.objects.get(id=data['story_id'])
        is_liked = True if checkLiked(story, request.user) else False
        if request.user.username != story.author.username:
            if not is_liked:  # Like action
                Likes(liked_by=request.user, to_Story=story).save()
                return JsonResponse({
                    'done': True,
                    'like_count': getLikeCount(story),
                    'old_button': 'fa-regular',
                    'new_button': 'fa-solid',
                    'Return Message': "Like Action is Done!",
                })

            else:  # Unlike Action
                Likes.objects.get(liked_by=request.user, to_Story=story).delete()
                return JsonResponse({
                    'done': True,
                    'like_count': getLikeCount(story),
                    'old_button': 'fa-solid',
                    'new_button': 'fa-regular',
                    'Return Message': "Unlike Action is Done!",
                })

        return JsonResponse({
            'done': False,
            'Error Message': "Users cannot Like their own stories",
        })


class Comment_action(LoginRequiredMixin, View):
    @staticmethod
    def post(request, *args, **kwargs):
        data = request.POST.dict()
        if not validateComment(data['current_username'], data['story_id']):
            return JsonResponse({
                'done': False,
                'errorMessage': "User name or story do not exist!"
            })

        createComment(data['comment'], data['current_username'], data['story_id']).save()

        return JsonResponse(
            {
                'done': True,
            })


class News_Feed(LoginRequiredMixin, View):
    @staticmethod
    def get(request, *args, **kwargs):

        num_elements = request.headers['num-elements']
        stories = get_story_details(get_story_list(request.user.id, num_elements))

        for i in range(stories.__len__()):
            stories[i][:1] = stories_to_list(stories[i][0])

        return JsonResponse({
            'done': True,
            "content": json.dumps(stories),
        })
