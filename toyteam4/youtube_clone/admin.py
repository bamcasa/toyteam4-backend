from django.contrib import admin
from .models import Video, Recommended_Videos, Comment, Reply

# Register your models here.

admin.site.register(Video)
admin.site.register(Recommended_Videos)
admin.site.register(Comment)
admin.site.register(Reply)
