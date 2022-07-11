from email.mime import application
import json
from wsgiref import headers
from phyDoc_app.models import Document_templates
from phyDoc_app.serializer import Document_templatesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from django.shortcuts import render, redirect

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
    
    
def insertDD(request):
    if request.method=="POST":
        id=request.POST.get('id')  
        templateid =request.POST.get('templateid')
        field_name =request.POST.get('field_name') 
        field_type =request.POST.get('field_type')   
        isRequired =request.POST.get('isRequired') 
        data={'id':id, 'templateid':templateid, 'field_name':field_name, 'field_type':field_type, 'isRequired':isRequired}
        headers={'Content-Type': 'application/json'}
        read= requests.post('http://127.0.0.1:8000/Document_details/CreateDD',json=data,headers=headers)
        return render(request,'insertdd.html')
    else:
        return render(request,'insertdd.html') 
   


