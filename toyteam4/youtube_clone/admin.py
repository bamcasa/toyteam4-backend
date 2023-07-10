from django.contrib import admin
from .models import Video, Comment, Reply, User

# Register your models here.

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(User)
