from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image

from ckeditor.fields import RichTextField


# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="images/")
    isi = RichTextField(blank=True, null=True)
    kategori = models.CharField(max_length=255)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

        img = Image.open(self.thumbnail.path)

        if img.height > 390 and img.width > 580:
            output_size = (580, 390)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

    def get_absolute_url(self):
        url_slug = {'slug': self.slug}
        return reverse('blog:detail', kwargs=url_slug)

    def __str__(self):
        return f"{self.id}.{self.judul}"
