# Generated by Django 2.2.12 on 2020-08-12 23:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200812_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='isi',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
