# Generated by Django 4.0.6 on 2022-07-10 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfollows',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='userfollows',
            name='followed_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(related_name='followed_users', through='authentication.UserFollows', to=settings.AUTH_USER_MODEL, verbose_name='abonnement'),
        ),
        migrations.AlterUniqueTogether(
            name='userfollows',
            unique_together={('user', 'followed_user')},
        ),
        migrations.RemoveField(
            model_name='userfollows',
            name='follower',
        ),
    ]