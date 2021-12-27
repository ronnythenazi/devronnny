from django.contrib import admin
# Register your models here.
from .models import BlogPost, regUser, Profile

admin.site.register(BlogPost)
admin.site.register(regUser)
admin.site.register(Profile)
