from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth import get_user_model




# Create your models here.


User = get_user_model()

class Contact(models.Model):
    user = models.OneToOneField(User, related_name='friends', on_delete=models.CASCADE, unique=True)

    friends = models.ManyToManyField('self', blank=True, null=True)

    def __str__(self):
        return self.user.username
