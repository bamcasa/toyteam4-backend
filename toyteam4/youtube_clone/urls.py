from django.urls import path
from .views import test, test_video, upload_video, view_video

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test/', test, name='test'),
    path('Videos/', test_video, name='Videos'),
    path('upload/', upload_video, name='upload'),
    path('view_video/<str:title>/', view_video, name='view_video'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
