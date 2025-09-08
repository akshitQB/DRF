from rest_framework import serializers
from .models import Students

class StudentSerializers(serializers.Serializer):
    roll_no = serializers.IntegerField()
    f_name = serializers.CharField(max_length=100)
    l_name = serializers.CharField(max_length=100)

    def  create(self,validate_data):
        return Students.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.f_name = validated_data.get('f_name', instance.f_name)
        instance.l_name = validated_data.get('l_name', instance.l_name)
        instance.save()
        return instance

