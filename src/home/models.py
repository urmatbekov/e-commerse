from django.db import models
from django.utils.translation import activate
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.safestring import mark_safe

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

    def image_tag(self):
        return mark_safe('<a href="{0}" target="_blank">'
                        '<img src="{1}" width="150" height="150" />'
                        '</a>'.format(self.image.url, self.image['admin_preview'].url)
                         )
    def image_icon(self):
        return mark_safe('<a href="{0}" target="_blank">'
                        '<img src="{1}" width="100" height="100" />'
                        '</a>'.format(self.image.url, self.image['admin_preview_icon'].url)
                         )