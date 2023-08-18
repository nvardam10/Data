from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet
from django.urls import path,include

urlpatterns = [
    path('', include('api.urls')),
]



