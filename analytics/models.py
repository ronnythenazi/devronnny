# analytics.models.py

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.db.models.signals import pre_save, post_save
from .utils import get_client_ip
from .signals import object_viewed_signal
from magazine.signals import user_visit_site
from users.signals import user_logged_in
from django.conf import settings
from django.contrib.auth.models import User
from magazine.models import BlogPost


FORCE_SESSION_TO_ONE = getattr(settings, 'FORCE_SESSION_TO_ONE', False)
FORCE_INACTIVE_USER_ENDSESSION = getattr(settings, 'FORCE_INACTIVE_USER_ENDSESSION', False)

class ObjectViewed(models.Model):
    user            = models.ForeignKey(User, blank=True, null=True, on_delete = models.CASCADE)
    content_type    = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id       = models.PositiveIntegerField()
    ip_address      = models.CharField(max_length=120, blank=True, null=True)
    content_object  = GenericForeignKey('content_type', 'object_id')
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self, ):
        return "%s viewed: %s" %(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'

def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    ip_address = None
    try:
        ip_address = get_client_ip(request)
    except:
        pass
    new_view_instance = ObjectViewed.objects.create(
                user=request.user,
                content_type=c_type,
                object_id=instance.id,
                ip_address=ip_address
                )

object_viewed_signal.connect(object_viewed_receiver)



class UserSession(models.Model):
    user            = models.ForeignKey(User, blank=True, null=True, on_delete = models.CASCADE)
    ip_address      = models.CharField(max_length=120, blank=True, null=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    session_key     = models.CharField(max_length = 100, blank= True, null = True)
    active          = models.BooleanField(default = True)
    ended           = models.BooleanField(default = False)


    def end_session(self):
        session_key = self.session_key
        try:
            Session.objects.get(pk=session_key).delete()
            self.active = False
            self.ended = True
            self.save()
        except:
            pass
        return self.ended


class PageVisitor(models.Model):
    session_key             = models.CharField(max_length=120, blank=True, null=True)
    page                    = models.ForeignKey(BlogPost, on_delete = models.CASCADE)
    first_time_visit        = models.DateTimeField(auto_now=True)
    LastTimeWasActive       = models.DateTimeField(auto_now_add=True)
    ip_address              = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        if(self.session_key != None):
            return "page:%s session_key:%s ip: %s first_time_visit:%s LastTimeWasActive %s" %(self.page.title, self.session_key , self.ip_address , self.first_time_visit, self.LastTimeWasActive)
        else:

            return "page:%s ip: %s first_time_visit:%s LastTimeWasActive %s" %(self.page.title, self.ip_address , self.first_time_visit, self.LastTimeWasActive)


class SiteVisitor(models.Model):
    session_key             = models.CharField(max_length=120, blank=True, null=True)
    first_time_visit        = models.DateTimeField(auto_now=True)
    LastTimeWasActive       = models.DateTimeField(auto_now_add=True)
    ip_address              = models.CharField(max_length=120, blank=True, null=True)


    def __str__(self):
        if(self.session_key != None):
            return "session_key:%s ip: %s first_time_visit:%s LastTimeWasActive %s" %(self.session_key , self.ip_address , self.first_time_visit, self.LastTimeWasActive)
        else:

            return "ip: %s first_time_visit:%s LastTimeWasActive %s" %(self.ip_address , self.first_time_visit, self.LastTimeWasActive)




def post_save_session_receiver(sender, instance, created, *args, **kwargs):
    if created:
        qs = UserSession.objects.filter(user=instace.user, ended=False, active=False).exclude(id=instance.id)
        for i in qs:
            i.end_session()
    if not instance.active and not instance.ended:
        instance.end_session()

if FORCE_SESSION_TO_ONE:
    post_save.connect(post_save_session_receiver, sender=UserSession)


def post_save_user_changed_receiver(sender, instance, created, *args, **kwargs):
    if not created:
        if instance.is_active == False:
            qs = UserSession.objects.filter(user, ended=False, active=False)
            for i in qs:
                i.end_session()

if FORCE_INACTIVE_USER_ENDSESSION:
    post_save.connect(post_save_user_changed_receiver, sender = User)



def user_visit_site_receiver(sender, instance, request, *args, **kwargs):
    session_key = request.session.session_key
    ip_address = get_client_ip(request)
    user = instance
    qs = UserSession.objects.filter(session_key = session_key, ip_address = ip_address, user=user)
    if qs.exists() == False:
        UserSession.objects.create(user=user, ip_address = ip_address, session_key = session_key)




user_visit_site.connect(user_visit_site_receiver)





def user_logged_in_receiver(sender, instance, request, *args, **kwargs):
    session_key = request.session.session_key
    ip_address = get_client_ip(request)
    user = instance
    qs = UserSession.objects.filter(session_key = session_key)
    for s_record in qs:
        s_record.delete()
    UserSession.objects.create(user=user, ip_address = ip_address, session_key = session_key)

user_logged_in.connect(user_logged_in_receiver)
