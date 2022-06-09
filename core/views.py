from django.shortcuts import render, HttpResponse
from django.template.context_processors import request

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('Hello {} de {} anos'.format(nome, idade))

def soma(request, numeroone, numerotwo):
    resultado = numeroone + numerotwo
    return HttpResponse('A soma dos numeros: {}'.format(resultado))

def subtracao(request, numeroone, numerotwo):
    resultado = numeroone - numerotwo
    return HttpResponse('A subtracao dos numeros: {}'.format(resultado))

def divisao(request, numeroone, numerotwo):
    resultado = numeroone / numerotwo
    return HttpResponse('A divisao dos numeros: {}'.format(resultado))

def multiplicacao(request, numeroone, numerotwo):
    resultado = numeroone * numerotwo
    return HttpResponse('A multiplicacao dos numeros: {}'.format(resultado))