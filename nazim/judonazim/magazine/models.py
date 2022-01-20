from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
exposed_request = None

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
    likes = models.ManyToManyField(User, related_name = "post_likes")
    dislikes = models.ManyToManyField(User, related_name = "post_dislikes")

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

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
    name = models.CharField(blank = False, max_length = 60, null = False)
    body = models.TextField(blank = False, null = False, max_length = 10000)
    comment_usr = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    date_added = models.DateTimeField(auto_now_add = True, blank = True)
    likes = models.ManyToManyField(User, related_name ="likes_com")
    dislikes = models.ManyToManyField(User, related_name ="dislikes_com")

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


    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class comment_of_comment(models.Model):
    comment = models.ForeignKey(Comment, related_name = "comments_of_comment" , on_delete = models.CASCADE)
    name = models.CharField(blank = False, max_length = 60, null = False)
    body = models.TextField(blank = False, null = False, max_length = 10000)
    comment_of_comment_usr = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    date_added = models.DateTimeField(auto_now_add = True, blank = True)

    likes = models.ManyToManyField(User, related_name ="likes_com_of_com")
    dislikes = models.ManyToManyField(User, related_name ="dislikes_com_of_com")

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

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s הגיב ל %s ב %s' % (self.comment.name, self.comment.post.title, self.comment.date_added)


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
    # 1=like, 2=comment, 3=follow, 4=dislike
    notification_type = models.IntegerField()
    to_user = models.ForeignKey(User, related_name = 'notification_to', on_delete = models.CASCADE, null = True)
    from_user = models.ForeignKey(User, related_name = 'notification_form' , on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(BlogPost, on_delete = models.CASCADE, related_name = '+', blank = True, null = True)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name = '+', blank = True, null = True)
    com_of_com = models.ForeignKey(comment_of_comment, on_delete = models.CASCADE, related_name = '+', blank = True, null = True)
    date = models.DateTimeField(default = timezone.now)
    user_has_seen = models.BooleanField(default = False)

    def __str__(self):
        return str(self.to_user.username) + '-type -' + str(self.notification_type) + 'date -' + str(self.date)
