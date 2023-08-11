from django.contrib.auth import get_user_model
from django.db import models
from users.models import Contact
User = get_user_model()





class Message(models.Model):
    contact = models.ForeignKey(
        Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username


class Chat(models.Model):
    participants = models.ManyToManyField(
        Contact, related_name='chats', blank=True,  null=True)
    messages = models.ManyToManyField(Message, blank=True, null=True)
    chat_name = models.CharField(blank = True, max_length = 200, null = True)

    def __str__(self):
        return "{}".format(self.pk)
