from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')  # Pagina Home

# def home(request):
#     return HttpResponse('Home')  # Pagina Home


def sobre(request):
    return HttpResponse('Sobre 1')  # Pagina Sobre


def contato(request):
    return HttpResponse('Contato 2')  # Pagina Contato
    # return HTTP Response
