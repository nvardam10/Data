from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserRegisterSerializer
from .models import UserDetails
# Create your views here.

class register(APIView):
    def get(self, request):
        # print('!!!!!!!!!!!!!!!!!!!')
        user = UserDetails.objects.all()
        serializer = UserRegisterSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request)
        serializer =UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

