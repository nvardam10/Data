from io import BytesIO
from django.shortcuts import render
# import io
from rest_framework.parsers import JSONParser
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import json


# Create your views here.
def user_api(request):
    if request.method == 'GET':
        jsondata = request.body
        # stream = BytesIO(json_data)
        json_data = json.loads(jsondata.decode('utf-8'))
        pythondata = JSONParser().parse(json_data)
        print(pythondata)
        id = pythondata.get('id',None)
        # req_body = json.loads(json_data)
        # id = req_body.get('id')
        if id is not None:
            use = User.objects.get(id=id)
            serializer = UserSerializer(use)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        use = User.object.all()
        serializer = UserSerializer(use,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

        
    
    
