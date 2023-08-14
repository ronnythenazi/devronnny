# Generated by Django 3.2.8 on 2023-08-13 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('chat', '0004_auto_20230813_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMsgNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_notifications', to='chat.chat')),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='message_notification', to='chat.message')),
                ('read_by_contacts', models.ManyToManyField(related_name='read_by_contacts', to='users.Contact')),
            ],
        ),
        migrations.DeleteModel(
            name='ChatNotifications',
        ),
    ]
