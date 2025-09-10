
from django.contrib import admin
from django.urls import path , include
# from .views import StudentListCreateView , StudentRetrieveUpdateDeleteView
from .views import StudentViewSet 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student_api' , StudentViewSet, basename='get-create')

urlpatterns = [
    # path('getdata/', StudentListCreateView.as_view()),
    # path('student/<int:pk>/',StudentRetrieveUpdateDeleteView.as_view()),
    
    # path('student/',StudentListCreateView.as_view()),
    # path('student/<int:pk>/',StudentRetriveUpdateDeleteView.as_view())
    
    path('',include(router.urls)),
    
]

