from email.mime import application
import json
from wsgiref import headers
from phyDoc_app.models import Document_templates
from phyDoc_app.serializer import Document_templatesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from django.shortcuts import render


def insertTemplate(request):
    if request.method=="POST":
        id=request.POST.get('id')  
        name=request.POST.get('name')   
        Document_template_path=request.POST.get('Document_template_path') 
        data={'id':id,'name':name,'Document_template_path':Document_template_path}
        headers={'Content-Type': 'application/json'}
        read= requests.post('http://127.0.0.1:8000/Document_templates/CreateDT',json=data,headers=headers)
        return render(request,'insert.html')
    else:
        return render(request,'insert.html')      


          


