from rest_framework import serializers
from api.models import User

#create serializers

class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50)
    email=serializers.CharField(max_length=50)
    phone=serializers.CharField(max_length=10)

    def create (self, validate_data):
        return S