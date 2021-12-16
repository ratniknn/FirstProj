from django.http import HttpResponse
from django.shortcuts import render

from .models import *

menu = {'Создать заявку', 'Заявки в работе', 'Выполненные заявки', 'Отчеты'}

def loginform(request):
    return render(request, 'task_board/loginform.html', {'menu': menu, 'title': 'Авторизация'})


def taskinwork(request):

    return render(request, 'task_board/taskinwork.html', {'menu': menu, 'title': 'Заявки в работе'})


