# Generated by Django 2.2.12 on 2020-08-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200815_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]