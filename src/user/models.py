from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'),unique=True, blank=True)
    avatar = ThumbnailerImageField(uploads_to="avatars",blank=True)