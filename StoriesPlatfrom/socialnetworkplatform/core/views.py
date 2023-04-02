from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'signin.html')


#This function is for signup
def signup(request):
    if request.method == 'POST':
        variablelist = [request.POST.get('Name Surname', False), request.POST['username'], request.POST['E-Mail address'],
                        request.POST['Password']]

        print(variablelist)
    else:
        return render(request, 'signup.html')

