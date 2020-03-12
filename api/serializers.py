# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import room,log
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = ['id', 'room', 'status', 'date_status']


class logSerializer(serializers.ModelSerializer):
    class Meta:
        model = log
        fields = ['id','room','status','date_status','ipaddress']

# from rest_framework import serializers
# from api.models import room,log


# class roomSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     room = serializers.CharField(required=False, allow_blank=False, max_length=100)
#     status = serializers.CharField(required=False, allow_blank=False, max_length=1)
#     date_status = serializers.DateTimeField(auto_add_now=True)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `room` instance, given the validated data.
#         """
#         instance.status = validated_data.get('status', instance.status)
#         instance.save()
#         return instance

# class logSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     room = serializers.CharField(required=False, allow_blank=False, max_length=100)
#     status = serializers.CharField(required=False, allow_blank=False, max_length=1)
#     date_status = serializers.DateTimeField(auto_add_now=True)
#     ipaddress = serializers.CharField(required=False, allow_blank=True, max_length=100)

#     def create(self, validated_data):
#     """
#     Create and return a new `log` instance, given the validated data.
#     """
#     return room.objects.create(**validated_data)