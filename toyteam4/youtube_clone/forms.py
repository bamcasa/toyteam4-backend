from django import forms
from .models import Video


class ImageForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'video_url', 'thumbnail')
