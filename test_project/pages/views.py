import re
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'
    # return HttpResponse({"Hello world"})


class AboutPage(TemplateView):
    template_name = 'about.html'
# Create your views here.
