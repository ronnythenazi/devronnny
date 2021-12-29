from django.contrib import admin
# Register your models here.
from .models import BlogPost, regUser, Profile, Comment

admin.site.register(BlogPost)
admin.site.register(regUser)
admin.site.register(Profile)
admin.site.register(Comment)
