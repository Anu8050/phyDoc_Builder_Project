from django.shortcuts import render
from django.http import HttpResponse
from .models import Document_templates

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the phyDoc index.")

def myview(request):
    #get your list of cities you may also do some filtering 
    templatesid = [obj.id for obj in Document_templates.objects.all()]
    return render(request, 'cities_template.html', {'templatesid': templatesid})