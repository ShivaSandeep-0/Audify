# Generated by Django 4.1.6 on 2023-06-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audify', '0005_video_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='subtitles_file',
            field=models.FileField(blank=True, upload_to='subtitles/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, upload_to='videos/'),
        ),
    ]
