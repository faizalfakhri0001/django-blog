# Generated by Django 2.2.12 on 2020-08-07 12:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200807_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='isi',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
