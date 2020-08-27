from django.db import models

from PIL import Image

from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Artikel

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(
        blank=True, null=True, upload_to="profile/", default='profile/default.jpg')
    Description = RichTextUploadingField(blank=True, null=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    website_name = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_name = models.CharField(max_length=255, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_name = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_name = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    github_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # img = Image.open(self.image.path)

        # if img.height > 300 and img.width > 300:
        #     output_size = (200, 200)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('profile')
