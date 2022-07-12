from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='Utilisateurs suivis: ',
        through='UserFollows',
        related_name='followed_users'
    )
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='Utilisateurs abonnés: ',
        through='UserFollowing',
        related_name='followed_by'
    )


class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed')

    class Meta:
        unique_together = ('user', 'followed_user')

class UserFollowing(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")
    following_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscribed")

    class Meta:
        unique_together = ('user', 'following_user')

