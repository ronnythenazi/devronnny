# Generated by Django 3.2.8 on 2023-08-06 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import magazine.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazine', '0118_auto_20230713_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_usr',
            field=models.ForeignKey(blank=True, default=magazine.models.get_default_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment_of_comment',
            name='comment_of_comment_usr',
            field=models.ForeignKey(blank=True, default=magazine.models.get_default_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_sub_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
