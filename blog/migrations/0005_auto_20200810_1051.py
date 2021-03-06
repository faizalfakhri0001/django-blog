# Generated by Django 2.2.12 on 2020-08-10 03:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_artikel_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'ordering': ('-published',)},
        ),
        migrations.AddField(
            model_name='artikel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artikel',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
