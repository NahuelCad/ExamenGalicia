from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Banco Galicia")


def hello(request):
    return render(request, 'index.html', {})
