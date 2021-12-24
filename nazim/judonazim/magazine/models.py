from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class BlogPost(models.Model):

    title = models.CharField(blank = False, max_length = 100, null = False, default = '')
    subtitle = models.CharField(blank = False, max_length = 200, null = False , default ='')
    thumb = models.ImageField(blank = False, null = False, upload_to = 'posts/images/%Y/%m/%d/')
    #author_name =  models.TextField(max_length = 50, null = false, default = "רוני הנאצי")
    author = models.ForeignKey(User, on_delete = models.CASCADE, default = 2,  blank = True)
    #author_email = models.EmailField(null = False, blank = True, default = "ronnythenazi@gmail.com")
    datepublished= models.DateField(auto_now_add = True, blank=True)
    datelastupdated= models.DateField(auto_now = True, blank=True)
    content =  RichTextField(blank = False, null = False) #models.TextField(null = False)
    public = "public"
    private = "private"
    #topic = models.TextField()
    #field publishstatus
    visibility = [

    (public , 'ציבורי'),
    (private, 'פרטי'),

    ]
    publishstatus = models.CharField(
        max_length = 10,
        choices=visibility,
        default=public,
        blank = False,
        )

    def get_absolute_url(self):
        return reverse('magazineNews')


class regUser(models.Model):
    email = models.EmailField(unique = True,  null = False, blank = False)
    nickname = models.CharField(max_length = 50, null = False)
#field userstatus
    active = "active"
    banned = "banned"
    deleted = "deleted"
    deactivated = "deactivate"
    status = [
    (active, "פעיל"),
    (banned, "הושבת"),
    (deleted, "נמחק"),
    (deactivated, "לא פעיל"),
    ]
    userstatus = models.CharField(
    max_length = 10,
    choices = status,
    default = active,
    )
# field usrrole

    typregular = "regular"
    typmoderator = "moderator"
    typeadmin = "admin"
    typeowner = "owner"

    roles = [
    (typregular, ""),
    (typmoderator, "מודרטור"),
    (typeadmin, "מנהל"),
    (typeowner, "מאסטר"),
    ]

    usrrole = models.CharField(max_length = 10, choices = roles, default = typregular)



class Moderators(models.Model):
    email = models.EmailField(unique = True,  null = False, blank = False)
