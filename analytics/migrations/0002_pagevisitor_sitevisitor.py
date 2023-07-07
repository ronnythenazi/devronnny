# Generated by Django 3.2.8 on 2023-07-05 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0110_profile_nick'),
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_time_visit', models.DateTimeField(auto_now=True)),
                ('LastTimeWasActive', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(blank=True, max_length=120, null=True)),
                ('session_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.usersession')),
            ],
        ),
        migrations.CreateModel(
            name='PageVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_time_visit', models.DateTimeField(auto_now=True)),
                ('LastTimeWasActive', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(blank=True, max_length=120, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine.blogpost')),
                ('session_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.usersession')),
            ],
        ),
    ]
