# Generated by Django 4.2.3 on 2023-07-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_clone', '0006_remove_recommended_videos_video_comment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_num',
            field=models.IntegerField(default=0, verbose_name='좋아요 수'),
        ),
        migrations.AddField(
            model_name='reply',
            name='like_num',
            field=models.IntegerField(default=0, verbose_name='좋아요 수'),
        ),
    ]
