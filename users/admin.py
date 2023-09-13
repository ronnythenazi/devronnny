from django.contrib import admin
from .models import (Contact, UserTokenKey, UserTokenPublicKey,)
# Register your models here.


admin.site.register(Contact)
admin.site.register(UserTokenKey)
admin.site.register(UserTokenPublicKey)
