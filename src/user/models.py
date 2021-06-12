from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, blank=True)
    avatar = ThumbnailerImageField(upload_to="avatars", blank=True)


class District(models.Model):
    name = models.CharField(max_length=120)


class ShippingAddress(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True)
    region = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    street = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BillingAddress(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True)
    region = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    street = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
