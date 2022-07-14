from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from phyDoc_app.models import Document_templates, Document_details
import requests
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the phyDoc index.")





