from django.urls import path
from .views import UserList, UserDetail, LocationList, LocationDetail,get_details

urlpatterns = [
    path('user/',UserList.as_view()),
    path('user/<int:pk>/',UserDetail.as_view()),
    path('location/',LocationList.as_view()),
    path('location/<int:pk>/',LocationDetail.as_view()),
    path('get-details/',get_details)
]
