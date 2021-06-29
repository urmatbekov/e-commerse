from django.db import models
from django.utils.translation import activate
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class Slider(models.Model):
    image = ThumbnailerImageField(upload_to="slider")
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title