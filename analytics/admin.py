from django.contrib import admin
from .models import ObjectViewed, UserSession, PageVisitor, SiteVisitor

# Register your models here.
admin.site.register(ObjectViewed)
admin.site.register(UserSession)
admin.site.register(PageVisitor)
admin.site.register(SiteVisitor)
