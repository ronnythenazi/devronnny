from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from social.calcs import get_total_seconds, get_curr_datetime
exposed_request = None


def get_time_gap_expired_seconds():
    return 3600

def is_edit_date_expired(com_date):
    curr_date = get_curr_datetime()
    gap = get_total_seconds(curr_date, com_date)
    if gap >= get_time_gap_expired_seconds():
        return True
    return False

def f_is_com_edited(date_added, date_edited):
    gap = get_total_seconds(date_edited, date_added)
    if gap > 1:
        return True
    return False

def get_default_user():
    user, created = User.objects.get_or_create(username = 'someone')
    user.set_password('Axu11P9$500192VzpoPapol@a')
    user.save()
    return user

class BlogPost(models.Model):

    title = models.CharField(blank = False, max_length = 60, null = False, default = '')
    subtitle = models.CharField(blank = False, max_length = 200, null = False , default ='')
    thumb = models.ImageField(blank = False, null = False, upload_to = 'posts/images/%Y/%m/%d/')
    #author_name =  models.TextField(max_length = 50, null = false, default = "רוני הנאצי")
    author = models.ForeignKey(User, on_delete = models.CASCADE,  default = 1,  blank = True)
    #author_email = models.EmailField(null = False, blank = True, default = "ronnythenazi@gmail.com")
    datepublished= models.DateTimeField(auto_now_add = True, blank=True)
    datelastupdated= models.DateTimeField(auto_now = True, blank=True)
    content =  RichTextField(blank = False, null = False) #models.TextField(null = False)
    likes = models.ManyToManyField(User, related_name = "post_likes", blank = True)
    dislikes = models.ManyToManyField(User, related_name = "post_dislikes", blank = True)
    followers = models.ManyToManyField(User, related_name = "post_followers", blank = True)

    def total_followers(self):
        return self.followers.count()

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def is_follow(self):
        if(self.followers.filter(id = exposed_request.user.id).exists()):
            return True
        return False

    public = "public"
    private = "private"



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

    def __str__(self):
        return '%s - %s' % (self.title, self.author.username)

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name = "comments" , on_delete = models.CASCADE)
    title = models.CharField(blank = True, max_length = 60, null = True, default = 'תגובה למאמר')
    body = RichTextField(blank = False, null = False, max_length = 10000)
    comment_usr = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, default = get_default_user)
    date_added = models.DateTimeField(auto_now_add = True, blank = True)
    date_last_update = models.DateTimeField(auto_now = True, null = True, blank = True)
    likes = models.ManyToManyField(User, related_name ="likes_com", blank = True)
    dislikes = models.ManyToManyField(User, related_name ="dislikes_com", blank = True)
    followers = models.ManyToManyField(User, related_name = "com_followers", blank = True)

    def total_followers(self):
        return self.followers.count()

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def liked(self):
        if(self.likes.filter(id = exposed_request.user.id).exists()):
            return True
        return False

    def disliked(self):
        if(self.dislikes.filter(id = exposed_request.user.id).exists()):
            return True
        return False

    def is_follow(self):
        if(self.followers.filter(id = exposed_request.user.id).exists()):
            return True
        return False

    def is_allowed_to_edit(self):
        return not is_edit_date_expired(self.date_added)

    def is_com_edited(self):
        return f_is_com_edited(self.date_added, self.date_last_update)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s - added at %s  last update at %s' % (self.post.title, self.comment_usr, self.date_added, self.date_last_update)

class comment_of_comment(models.Model):
    comment = models.ForeignKey(Comment, related_name = "comments_of_comment" , on_delete = models.CASCADE)
    title = models.CharField(blank = True, max_length = 60, null = True)
    body = RichTextField(blank = False, null = False, max_length = 10000)
    comment_of_comment_usr = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, default = get_default_user)
    to_sub_comment = models.ForeignKey('comment_of_comment', on_delete = models.CASCADE, related_name = 'replied_to', blank = True, null = True)
    date_added = models.DateTimeField(auto_now_add = True, blank = True)
    date_last_update = models.DateTimeField(auto_now = True, null = True, blank = True)
    likes = models.ManyToManyField(User, related_name ="likes_com_of_com", blank = True)
    dislikes = models.ManyToManyField(User, related_name ="dislikes_com_of_com", blank = True)

    followers = models.ManyToManyField(User, related_name = "sub_com_followers", blank = True)

    def total_followers(self):
        return self.followers.count()

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def liked(self):
        if(self.likes.filter(id = exposed_request.user.id).exists()):
            return True
        return False

    def disliked(self):
        if(self.dislikes.filter(id = exposed_request.user.id).exists()):
            return True
        return False

    def is_follow(self):
        if(self.followers.filter(id = exposed_request.user.id).exists()):
            return True
        return False

    def is_allowed_to_edit(self):
        return not is_edit_date_expired(self.date_added)

    def is_com_edited(self):
        return f_is_com_edited(self.date_added, self.date_last_update)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s הגיב ל %s ב %s' % (self.comment_of_comment_usr, self.comment.post.title, self.comment.date_added)


class Profile(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 1000, null = True, blank = True)
    profile_img =  models.ImageField(default="default.jpg", blank = True, null = True, upload_to = 'members/profile/avatar')

    first_name = models.CharField(max_length = 100, null = True, blank = True)
    last_name = models.CharField(max_length = 100, null = True, blank = True)
    race = models.CharField(max_length = 200, null = True, blank = True)
    y_dna = models.CharField(max_length = 200, null = True, blank = True)
    mtdna = models.CharField(max_length = 200, null = True, blank = True)
    birthDate = models.DateField(null = True, blank = True)
    joinDate = models.DateField(auto_now_add = True, blank = True)

    male = 'male'
    female = 'female'
    sex_choices = [(male, 'גבר' ), (female, 'נקבה')]
    sex = models.CharField(null = True, blank = True, choices = sex_choices, max_length = 30)

    politic_views = models.CharField(null = True, blank = True, max_length = 200)
    religion = models.CharField(null = True, blank = True, max_length = 100)
    education = models.TextField(null = True, blank = True, max_length = 200)
    slogan = models.TextField(null = True, blank = True, max_length = 1000)

    single = 'single'
    married = 'married'
    divorced = 'divorced'
    married_again = 'married_again'

    status_list = [(single , 'רווק'), (married , 'נשוי'), (divorced , 'גרוש'), (married_again , 'נשוי פעם נוספת')]

    familial_status = models.CharField(null = True, blank = True, choices = status_list, max_length = 100)

    followers = models.ManyToManyField(User, related_name ="followers")
    following = models.ManyToManyField(User, related_name = "following")

    def total_followers(self):
        return self.followers.count()

    def total_following(self):
        return self.following.count()

    def __str__(self):
        return str(self.user)


class Album(models.Model):

    profile = models.ForeignKey(Profile, related_name = 'profile_album', on_delete = models.CASCADE)
    description = models.CharField(max_length = 500, null = True, blank = True)
    myfile = models.ImageField(null = False, blank = False,  upload_to = 'album/%Y/%m/%d')
    upload_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(self.profile.user.username) + '-' + str(self.description)



class Notification(models.Model):
    # 1=like, 2=comment, 3=follow user, 4=dislike, 5=com on post you are follow,
    # 6=sub_com on post you are follow, #7 sub_com on com you are follow, 8 = tag
    # 9=post published

    notification_type = models.IntegerField()
    to_user = models.ForeignKey(User, related_name = 'notification_to', on_delete = models.CASCADE, null = True)
    from_user = models.ForeignKey(User, related_name = 'notification_form' , on_delete = models.CASCADE, null = True, default = get_default_user)
    post = models.ForeignKey(BlogPost, on_delete = models.CASCADE, related_name = '+', blank = True, null = True)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name = '+', blank = True, null = True)
    com_of_com = models.ForeignKey(comment_of_comment, on_delete = models.CASCADE, related_name = '+', blank = True, null = True)
    date = models.DateTimeField(default=timezone.now)
    user_has_seen = models.BooleanField(default = False)



    def __str__(self):
        return str(self.to_user.username) + '-type -' + str(self.notification_type) + 'date -' + str(self.date)
