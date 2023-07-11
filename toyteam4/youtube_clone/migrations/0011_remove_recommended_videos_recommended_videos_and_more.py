# Generated by Django 4.2.3 on 2023-07-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_clone', '0010_remove_video_recommended_video_recommended_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommended_videos',
            name='recommended_videos',
        ),
        migrations.AddField(
            model_name='recommended_videos',
            name='recommended_videos',
            field=models.ManyToManyField(null=True, related_name='recommended_videos', to='youtube_clone.video'),
        ),
    ]
