from django.http import HttpResponse
from django.shortcuts import render


def loginform(request):
    return HttpResponse("Страница входа")


def taskinwork(request):
    return HttpResponse("Заявки в работе")


