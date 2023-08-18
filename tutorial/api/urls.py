from django.urls import path
from .views import *
urlpatterns = [
    path('register',register.as_view()),
    # path('validate-user/<int:pk>/',validate_user),
    # path('booking',book_movie)
]