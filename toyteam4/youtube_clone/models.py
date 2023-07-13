from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(
        verbose_name='프로필 설정', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='계정 생성 날짜', auto_now_add=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # video_file = models.FileField(upload_to='videos/')
    video_url = models.CharField(max_length=100, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    view_count = models.IntegerField(verbose_name='조회수', default=0)
    

    def __str__(self):
        return self.title


class Recommended_Videos(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE,related_name='original_videos' )
    # selected_video = models.ForeignKey(Video, on_delete=models.CASCADE)
    recommended_videos = models.ManyToManyField(
        Video, related_name='recommended_videos')


class Comment(models.Model):
    name = models.CharField(max_length=100, default='' )
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    like_num = models.IntegerField(verbose_name="좋아요 수", default=0)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    like_num = models.IntegerField(verbose_name="좋아요 수", default=0)
