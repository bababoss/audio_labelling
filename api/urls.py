from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('audio/', views.Annatotaion.as_view(), name='Annatotaion'),
    path('upload/', views.UploadMedia.as_view(), name='UploadMedia'),
    path('audio_list/', views.AudioList.as_view(), name='AudioList'),


]

