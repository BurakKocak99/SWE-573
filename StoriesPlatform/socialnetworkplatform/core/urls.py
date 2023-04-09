from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.signup, name='signup'),
    path('post', views.create_post, name='create_post'),
    path('editprofile/<slug:slug>/', views.edit_profile, name='edit_profile'),
]
