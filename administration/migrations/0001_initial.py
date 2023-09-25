# Generated by Django 3.2.8 on 2023-09-25 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=30)),
                ('groupDescription', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hideComment', models.BooleanField(default=False)),
                ('seeHiddenComments', models.BooleanField(default=False)),
                ('removeComment', models.BooleanField(default=False)),
                ('banUsers', models.BooleanField(default=False)),
                ('suspendUsers', models.BooleanField(default=False)),
                ('unbanUsers', models.BooleanField(default=False)),
                ('deleteAllcomments', models.BooleanField(default=False)),
                ('hideAllcomments', models.BooleanField(default=False)),
                ('createLabels', models.BooleanField(default=False)),
                ('removeLabels', models.BooleanField(default=False)),
                ('pinComments', models.BooleanField(default=False)),
                ('unpinComments', models.BooleanField(default=False)),
                ('deleteUsers', models.BooleanField(default=False)),
                ('lockComment', models.BooleanField(default=False)),
                ('disableComments', models.BooleanField(default=False)),
                ('sendSiteNotifications', models.BooleanField(default=False)),
                ('managePermissionGroups', models.BooleanField(default=False)),
                ('manageUserPermissions', models.BooleanField(default=False)),
                ('group', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.permissiongroup')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='rights',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('group__isnull', False), ('user', None)), models.Q(('group', None), ('user__isnull', False)), _connector='OR'), name='not_both_group_and_user_null'),
        ),
    ]
