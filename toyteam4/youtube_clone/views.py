from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Video

from .forms import ImageForm

# Create your views here.


def test(request):
    return HttpResponse("It is TEST page")


def test_video(request):
    videos = Video.objects.all()
    return render(request, 'Videos.html', {'videos': videos})


def upload_video(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Videos')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def view_video(request, title):
    video = Video.objects.get(title=title)
    return render(request, 'view_video.html', {'video': video})
