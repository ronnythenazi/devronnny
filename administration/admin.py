from django.contrib import admin
from .models import (PermissionGroup, Rights,)

# Register your models here.

admin.site.register(PermissionGroup)
admin.site.register(Rights)
