# Generated by Django 4.2.2 on 2023-07-05 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_clone', '0004_user_remove_recommended_videos_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='reply',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='recommended_videos',
            name='user',
        ),
        migrations.AddField(
            model_name='recommended_videos',
            name='video',
            field=models.ManyToManyField(to='youtube_clone.video'),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='계정 생성 날짜'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='프로필 설정'),
        ),
        migrations.AddField(
            model_name='video',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='조회수'),
        ),
    ]
