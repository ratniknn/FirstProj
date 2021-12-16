from django.urls import path

from .views import *

urlpatterns = [
    path('', loginform, name='loginform'),
    path('taskinwork/', taskinwork, name='taskinwork'),
]