from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Create your models here.


class PermissionGroup(models.Model):
    groupName         = models.CharField(max_length = 30)
    groupDescription  = models.CharField(max_length = 30, null= True)

    def __str__(self):
        return 'group name: %s description %s ' % (self.groupName, self.groupDescription)



class Rights(models.Model):
    group            = models.OneToOneField(PermissionGroup, null = True, related_name ="permissions", on_delete = models.CASCADE)
    user             = models.OneToOneField(User, null = True, related_name ="rights", on_delete = models.CASCADE)

    hideComment                    = models.BooleanField(default=False)
    unhideComment                  = models.BooleanField(default=False)
    seeHiddenComments              = models.BooleanField(default=False)
    removeComment                  = models.BooleanField(default=False)
    banUsers                       = models.BooleanField(default=False)
    suspendUsers                   = models.BooleanField(default=False)
    unbanUsers                     = models.BooleanField(default=False)
    deleteAllcomments              = models.BooleanField(default=False)
    hideAllcomments                = models.BooleanField(default=False)
    createLabels                   = models.BooleanField(default=False)
    removeLabels                   = models.BooleanField(default=False)
    pinComments                    = models.BooleanField(default=False)
    unpinComments                  = models.BooleanField(default=False)
    deleteUsers                    = models.BooleanField(default=False)
    lockComment                    = models.BooleanField(default=False)
    disableComments                = models.BooleanField(default=False)
    sendSiteNotifications          = models.BooleanField(default=False)
    managePermissionGroups         = models.BooleanField(default=False)
    manageUserPermissions          = models.BooleanField(default=False)


    def __str__(self):
        if   self.user is not None:
            return 'username: %s ' % (self.user.username)
        return 'group name: %s description %s ' % (self.group.groupName, self.group.groupDescription)


    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(group__isnull=False, user=None) | Q(group=None, user__isnull=False),
                name='not_both_group_and_user_null'
            )
        ]
