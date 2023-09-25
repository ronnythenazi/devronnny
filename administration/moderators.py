from .utils import hideComObj, unhideComObj
from .models import (PermissionGroup, Rights,)



def hideCom(objName, id, user):
    if(isUserAllowed('hideComment', user) == False):
        return False
    hideComObj(objName, id)
    return True

def unhideCom(objName, id, user):
    if(isUserAllowed('unhideComment', user) == False):
        return False
    unhideComObj(objName, id)


def isUserAllowed(permissionName, user):
    if(Rights.objects.filter(user=user).exists()):
        return Rights.objects.filter(user=user).values_list(permissionName,flat=True)[0]
    return Rights.objects.filter(group=user.profile.role).values_list(permissionName,flat=True)[0]
