from django.urls import path

from .views import *

urlpatterns = [
    path('', loginform),
    path('taskinwork/', taskinwork),
]