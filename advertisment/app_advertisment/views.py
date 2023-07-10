from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Это мой первый сайт!</h1>')


# Create your views here.
#отправляет на наши запросы обычные html-страницы

