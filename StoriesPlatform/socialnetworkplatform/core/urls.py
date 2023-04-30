from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.signup, name='signup'),
    path('post', views.create_post, name='create_post'),
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('viewprofile/<slug:slug>/', views.viewprofile, name='viewprofile'),
    path('follow/<slug:slug>',  views.FollowToggle.as_view(), name='follow'),
    path('network/<slug:slug>', views.follower_page, name= 'network'),
]
