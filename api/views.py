
###############################TRest framework #########################
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.parsers import FileUploadParser, MultiPartParser,JSONParser

########################## import   Model #################################
from api import models
######################### import serializers ###########################
from api import serializers

##################Utiliyties#############################################
import json,requests,os,sys,uuid
from django.http import HttpResponse

class AudioList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        model_obj = models.MediaFileUpload.objects.all()
        serializer = serializers.MediaFileUploadSerializer(model_obj, many=True)
        return  Response(serializer.data)

class Annatotaion(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    parser_classes = (JSONParser,MultiPartParser,)
    def post(self, request, format=None):
        try:
            #email = request.query_params["email"]
            filename = request.data["filename"]
            text = request.data['text']
        except:
            filename=None
            text=None

        print("filename: ",filename,text)
        if filename and text:
            media_obj=models.MediaFileUpload.objects.get(filename)
            media_obj.text=text
            media_obj.is_label=True
            media_obj.save()

            RESPONSE = {"success": True,
                        "response":"hsdjfhhjsgfjhsdgjhsfjsdhgkjsdf"}
            return Response(RESPONSE,status=status.HTTP_200_OK)
        RESPONSE = {"success": False,
                    "response":"Not found" }
        return Response()
    
    

class UploadMedia(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    parser_classes = (JSONParser,MultiPartParser,)
    def post(self, request, format=None):
        try:
            media_file = request.data['filename']
        except:
            media_file=None


        if media_file:
            media_obj=models.MediaFileUpload.objects.create(media_file=media_file)
            media_obj.save()

            RESPONSE = {"success": True,
                        "response":"hsdjfhhjsgfjhsdgjhsfjsdhgkjsdf"}
            return Response(RESPONSE,status=status.HTTP_200_OK)
        RESPONSE = {"success": False,
                    "response":"Not found" }
        return Response()
