import re
from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse({"Hello world"})

# Create your views here.
