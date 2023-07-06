from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import *
from .models import User, Video, Recommended_Videos, Comment, Reply
# Create your views here.


def test(request):
    return HttpResponse("It is TEST page")


def test_video(request):
    videos = Video.objects.all()
    return render(request, 'Videos.html', {'videos': videos})


class UserViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = UserSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = VideoSerializer

class Recommended_VideosViewSet(viewsets.ModelViewSet):
    queryset = Recommended_Videos.objects.all()
    serializer_class = Recommended_VideoSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer