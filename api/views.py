
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
from django.shortcuts import render

def index(request):
    return render(request, 'api/index.html', {})

class AudioList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        model_obj = models.MediaFileUpload.objects.filter(is_label=False)
        serializer = serializers.MediaFileUploadSerializer(model_obj, many=True)
        data_dict={}
        for i in serializer.data[0]:
            if i=='media_file':
                data_dict[i]="http://127.0.0.1:8000"+serializer.data[0][i]
            else:
                data_dict[i] = serializer.data[0][i]

        return  Response(data_dict)

class Annatotaion(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    #parser_classes = (JSONParser,MultiPartParser,)
    def post(self, request, format=None):

        #email = request.query_params["email"]
        filename = request.data["filename"]
        #filename="uploaded_media/LJ040-0107.wav"
        text = request.data['text']
        print("data: --------------------",request.data)
        print("text - - - - - - -  - - -  -", text)


        print("filename: ",filename,text)
        if filename and text:
            media_obj=models.MediaFileUpload.objects.get(media_file="uploaded_media/"+os.path.split(filename)[-1])
            media_obj.text=text
            media_obj.is_label=True
            media_obj.save()

            RESPONSE = {"success": True,
                        "response":{"path":str(media_obj.media_file),"text":str(media_obj.text)}}
            return Response(RESPONSE,status=status.HTTP_200_OK)
        RESPONSE = {"success": False,
                    "response":"Not found" }
        return Response(RESPONSE)
    
    

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
                        "response":str(media_obj.media_file)}
            return Response(RESPONSE,status=status.HTTP_200_OK)
        RESPONSE = {"success": False,
                    "response":"Not found" }
        return Response()
