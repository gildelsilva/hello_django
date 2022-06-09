from django.shortcuts import render, HttpResponse
from django.template.context_processors import request

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('Hello {} de {} anos'.format(nome, idade))