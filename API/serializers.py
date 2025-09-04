from rest_framework import serializers
from .models import Students

class StudentSerializers(serializers.Serializer):
    Roll_no = serializers.IntegerField()
    F_name = serializers.CharField(max_length=100)
    L_name = serializers.CharField(max_length=100)
