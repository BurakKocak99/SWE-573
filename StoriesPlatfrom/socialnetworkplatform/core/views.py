from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import login,logout, authenticate
# Create your views here.


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
            return redirect('')
        else:
            print("Form is not valid!")
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form})
