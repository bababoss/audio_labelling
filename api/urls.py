from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api import views


urlpatterns = [
    path('inhouse/', views.inhouse, name='index'),
    path('', views.index, name='index'),

    path('labelinhouse/', views.AnnatotaionInhouse.as_view(), name='AnnatotaionInhouse'),
    path('upload/', views.UploadMedia.as_view(), name='UploadMedia'),
    path('upload/model/', views.UploadModel.as_view(), name='UploadModel'),
    path('label/', views.Annatotaion.as_view(), name='Annatotaion'),
    path('audio_list/', views.AudioList.as_view(), name='AudioList'),
    path('model_list/', views.ModelList.as_view(), name='ModelList'),


]

if True:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

