from django.contrib import admin
# Register your models here.
from .models import BlogPost, regUser, Profile, Comment, comment_of_comment, Notification

admin.site.register(BlogPost)
admin.site.register(regUser)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(comment_of_comment)
admin.site.register(Notification)
