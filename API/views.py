from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Students
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse , JsonResponse

def getdetails(request,pk):
    stu = Students.objects.get(id=pk)
    serialize = StudentSerializers(stu)
    json_data = JSONRenderer().render(serialize.data)

    return JsonResponse(serialize.data)