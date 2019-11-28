from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(blank=False, null=False, max_length=100)

    def to_dict(self):
        return {
            'user': self.user.id,
            'username': self.user.username,
            'nickname': self.nickname,
        }


class Client(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            'user': self.user.id,
            'username': self.user.username,
            'clientname': self.client.name,
        }
