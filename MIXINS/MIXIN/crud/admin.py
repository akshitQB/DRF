from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','gr_no','stu_name','stu_class','stu_email']
    class Meta():
        model = Student
