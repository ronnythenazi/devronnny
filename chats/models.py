from django.contrib.auth import get_user_model
from django.db import models
from users.models import Contact
User = get_user_model()








class Chat(models.Model):
    participants = models.ManyToManyField(
        Contact, related_name='chats', blank=True)


    chat_name = models.TextField(blank = True, null = True)


    def __str__(self):
        return "{}".format(self.pk)


class Message(models.Model):
    contact = models.ForeignKey(
        Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, related_name="messages", on_delete = models.CASCADE)

    def __str__(self):
        return self.contact.user.username


class ChatMsgNotification(models.Model):
    chat = models.ForeignKey(Chat, related_name="chat_notifications", on_delete = models.CASCADE)
    message =  models.OneToOneField(Message, related_name="message_notification", on_delete=models.CASCADE)
    read_by_contacts = models.ManyToManyField(Contact, related_name="read_by_contacts")

    def get_from_username(self):
        username =  self.message.contact.username
        return username


    def get_to_username(self):
        from_username = self.get_from_username()
        qs = self.chat.participants.filter(contact__username != from_username).first()
        return qs[0].username

    def __str__(self):
        return "from: {from_user} to: {to} message {msg} timestamp {time}".format(from_user = self.get_from_username(),
        to = self.get_to_username, msg = self.message.content, time = self.message.timestamp)
