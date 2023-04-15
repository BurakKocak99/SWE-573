from django.shortcuts import render, redirect
from .forms import RegistrationForm, PostForm, EditProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Profile, Story, Comment
from .util import CreateProfile


# Create your views here.

@login_required(login_url="/login")
def home(request):
    return render(request, 'home.html')


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
def edit_profile(request, slug):
    profile = Profile.objects.get(Username=slug)
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
    stories = Story.objects.all().filter(author_id=request.user)
    context = {
        'stories': stories,
        'username': slug,
        'follower': 33, # to be added dynamically later
        'following': 40, # to be added dynamically later
    }
    return render(request, 'profile/view_profile.html', context=context)

