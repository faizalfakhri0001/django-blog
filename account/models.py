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
    image = models.ImageField(blank=True, null=True, upload_to="profile/")
    Description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    def save(self):
        super().save()

        # print(self.image.path)
        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id})
