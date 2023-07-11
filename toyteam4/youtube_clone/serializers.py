from rest_framework import serializers
from .models import User, Video, Recommended_Videos, Comment, Reply


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class Recommended_VideoSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.name')
    recommended_videos = VideoSerializer(many=True)

    class Meta:
        model = Recommended_Videos
        # fields = '__all__'
        fields = ['recommended_videos']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
