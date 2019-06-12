from rest_framework import serializers
from api import models

class MediaFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.MediaFileUpload
        fields=('id','media_file','text','is_label','created')
        
class ModelFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ModelFileUpload
        fields=('id','model_file','discription','created')