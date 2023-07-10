from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import test, test_video
from .views import *

from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'replies', ReplyViewSet)
router.register(r'rdvideos', Recommended_VideosViewSet,
                basename='recommended-videos')


urlpatterns = [
    path('test/', test, name='test'),
    path('Videos/', test_video, name='Videos'),
    # path('upload/', upload_video, name='upload'),
    # path('view_video/<str:title>/', view_video, name='view_video'),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
