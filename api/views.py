
###############################TRest framework #########################
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.parsers import FileUploadParser, MultiPartParser,JSONParser

########################## import   Model #################################
from accenture_app import models
######################### import serializers ###########################
from accenture_app import serializers

##################Utiliyties#############################################
import json,requests,os,sys,uuid
from utilities import audio_spliter as spliter
from utilities import audio_spliter ,request_utils, video_decomposer,media_metadata,result_utils,db_obj_utils,redis_broker,post_json_process,post_result_processing
from accenture_app import scene,object_detector,face,speech,tasks


from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class UploadMedia(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    parser_classes = (JSONParser,MultiPartParser,)
    def post(self, request, format=None):
        try:
            #email = request.query_params["email"]
            email = request.data["email"]
            media_file = request.data['media_file']
        except:
            email=None
            media_file=None
        language_type="english"
        try:
            language_type = request.data['language_type']
        except:
            pass
        print("email: ",email)
        if email and media_file:
            usr=db_obj_utils.user_object(email)
            print(usr.email)
            media_obj=media_metadata.save_media(media_file,usr)['db_obj']
            media_obj.language=language_type
            media_obj.save()
            print("media_objmedia_objmedia_objmedia_obj: ",media_obj.media_file,"fsdfs ",int(media_obj.id))
            run_all_model(media_obj,email,language_type=language_type)
            RESPONSE = {"success": True,
                        "response":{"video_id":str(media_obj.id),"message":"Video uploaded successfully. You will get mail soon"} }
            return Response(RESPONSE,status=status.HTTP_200_OK)
        RESPONSE = {"success": False,
                    "response":"Not found" }
        return Response()
