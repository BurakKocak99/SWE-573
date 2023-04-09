from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, PostForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def home(request):
    return render(request, 'home.html')




#This function is for signup
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
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
            print(story.placeID)
            story.save()
            return redirect('home')
        else:
            print("Post Form was not valid!!!")
    else:
        form = PostForm()

    return render(request, 'Post/create_post.html', {"form": form})
