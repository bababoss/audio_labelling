from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api import views


urlpatterns = [
    path('annotation/', views.index, name='index'),
    path('upload/', views.UploadMedia.as_view(), name='UploadMedia'),
    path('label/', views.Annatotaion.as_view(), name='Annatotaion'),
    path('audio_list/', views.AudioList.as_view(), name='AudioList'),


]

if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

