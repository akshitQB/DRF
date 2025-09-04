from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Students
from rest_framework.renderers import JSONRenderer 
import io
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


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