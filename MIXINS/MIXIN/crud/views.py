from django.shortcuts import render
from rest_framework import generics , mixins , viewsets
from .serializers import StudentSerializer
from .models import Student



# class StudentListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):

#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self , request , *args , **kwargs):
#         return self.list(request , *args , **kwargs)
    
#     def post(self , request , *args , **kwargs):
#         return self.create(request , *args , **kwargs)


# class StudentRetrieveUpdateDeleteView(mixins.RetrieveModelMixin,
#                                       mixins.UpdateModelMixin,
#                                       mixins.DestroyModelMixin,
#                                       generics.GenericAPIView):
    
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self , request , *args , **kwargs):
#         return self.retrieve(request , *args , **kwargs)
    
#     def put(self , request , *args , **kwargs):
#         return self.update(request , *args , **kwargs)
    
#     def delete(self , request , *args , **kwargs):
#         return self.destroy(request , *args , **kwargs)


#this one is viewset 
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#concrete Views in DRF 
#List all students Or Create a new Student
    class StudentListCreateView(generics.ListCreateAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer


    # Retrieve , Update or Delete a Student 
    class StudentRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
