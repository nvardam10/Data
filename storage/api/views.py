from rest_framework import generics
from .models import User, Location
from .serializers import UserSerializer, LocationSerializer
from django.http import JsonResponse
import json,requests

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(userLocation=location)
        return queryset
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

def get_details(request):
    # print('111111111111111111')
    print(request.headers)
    request_object=json.loads(request.body)
    return_object= {"details":request_object['name']}
    return JsonResponse(return_object,safe=False)