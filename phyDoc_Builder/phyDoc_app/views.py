from django.shortcuts import render
from django.http import HttpResponse
from .models import Document_templates
from django.http import HttpResponseRedirect
from .serializer import Document_templatesSerializer
from django.views import generic
from phyDoc_app.models import Document_templates, Document_details
import requests
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the phyDoc index.")

