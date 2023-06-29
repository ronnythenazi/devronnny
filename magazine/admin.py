from django.contrib import admin
# Register your models here.
from .models import BlogPost, Profile, Comment, comment_of_comment, Notification, Album, Labels

admin.site.register(BlogPost)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(comment_of_comment)
admin.site.register(Notification)
admin.site.register(Album)
admin.site.register(Labels)
