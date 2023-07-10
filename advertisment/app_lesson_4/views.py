from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h2>Домашка по 4 занятию</h2>')

