from rest_framework.parsers import JSONParser 
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from testapi.models import personal_data
from . serializer import dataSerializer
import json

@api_view(['GET'])
def get_data(request):
    if request.method=='GET':
        x=personal_data.objects.all()
        sz=dataSerializer(x, many=True)
        return Response(sz.data)

@api_view(['POST'])
def ins_data(request):
    if request.method=='POST':
        json_data = JSONParser().parse(request)
        tutorial_serializer = dataSerializer(data=json_data)
        if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return Response({'Success':"Data Inserted !"})

@api_view(['DELETE'])
def del_data(request):
    if request.method=='DELETE':
        json_body=request.body.decode('utf-8')
        data=json.loads(json_body)
        email=data['email']
        personal_data.objects.filter(email=email).delete()
        return Response({'Message':'Object deleted successfully !'})

@api_view(['PUT'])
def update_data(request):
    if request.method=='PUT':
        json_data = JSONParser().parse(request)
        data=personal_data.objects.get(id=json_data['id'])
        ser=dataSerializer(data, data=json_data, partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"Message":"Updated successfully !"})
        return JsonResponse({"Error":"Something went erong !"})


