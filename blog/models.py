from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(blank=True, editable=False)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.name}"

    def save(self):
        self.slug = slugify(self.name)
        super().save()


class Artikel(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    judul = models.CharField(max_length=255)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="images/")
    isi = RichTextUploadingField(blank=True, null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='artikel')
    kategori = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='artikel')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-published',)

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
        return f"{self.judul}"
