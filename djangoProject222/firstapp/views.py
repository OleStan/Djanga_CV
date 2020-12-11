from urllib import request

from django.template.response import TemplateResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def index2(reguest):
    return render(request, "index2.html")