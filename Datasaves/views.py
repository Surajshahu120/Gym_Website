from django.shortcuts import render
from django.http import HttpResponse


def human(request):
    return HttpResponse('My name is suraj')
