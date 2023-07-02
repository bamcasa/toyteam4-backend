from django.shortcuts import render
from django.http import HttpResponse

from .models import Video
# Create your views here.


def test(request):
    return HttpResponse("It is TEST page")


def test_video(request):
    videos = Video.objects.all()
    return render(request, 'Videos.html', {'videos': videos})
