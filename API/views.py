from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Students
from rest_framework.renderers import JSONRenderer 
import io
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def getdetails(request,pk):
    stu = Students.objects.get(id=pk)
    serialize = StudentSerializers(stu)
    json_data = JSONRenderer().render(serialize.data)

    return JsonResponse(json_data)
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer  = StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    

    stu = Students.objects.all()
    serialize = StudentSerializers(stu, many=True)
    json_data = JSONRenderer().render(serialize.data)
    return HttpResponse(json_data , content_type='application/json')
    
@csrf_exempt
def student_update(request):
    if request.method == "PUT":
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Students.objects.get(id=id)
        serialize =  StudentSerializers(stu , data =pythondata ,  partial=True)

        if serialize.is_valid():
            serialize.save()
            res = {
                'msg' : 'Data has been updated'
            }
            json_data =  JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
    
@csrf_exempt
def student_delete(request):
    if request.method == "DELETE":
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Students.objects.get(id=id)
        stu.delete()
        res = {'msg' : 'Data has been deleted....'}
        json_data = JSONRenderer().render(res)
        return JsonResponse(res, safe=False)

