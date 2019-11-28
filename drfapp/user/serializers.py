from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=True, max_length=150)
    nickname = serializers.CharField(required=True, allow_blank=True, max_length=100)


class EmployeeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=True, max_length=150)
    clientname = serializers.CharField(required=True, allow_blank=True, max_length=100)
