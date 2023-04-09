from django.contrib import admin
from .models import Profile, Story, Comment
# Register your models here.

admin.site.register(Profile)
admin.site.register(Story)
admin.site.register(Comment)