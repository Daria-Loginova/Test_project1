from django.shortcuts import render
from django.http import HttpResponse


# def hello_word(request):
#     return HttpResponse("<h1><br>my name is Daria<br/><h1/>")


def index(request):
    return render(request, 'index.html', {})
