from django.contrib import admin
from .models import Students


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['Roll_no' , 'F_name','L_name']
    class Meta():
        model= Students
    
