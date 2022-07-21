from email.mime import application
import json
from wsgiref import headers
from phyDoc_app.models import Document_templates, Document_details
from phyDoc_app.serializer import Document_templatesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
#generating a pdf file
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.files.storage import FileSystemStorage

def insertTemplate(request):
    if request.method=='POST':
        name=request.POST['name']   
        Document_template_path=request.FILES['Document_template_path']
        object=Document_templates.objects.create(name=name, Document_template_path=Document_template_path)
        object.save()  
    context=Document_templates.objects.all()
    return render(request,'insert.html',{'context':context})

def insertDD(request):
    results=Document_templates.objects.all
    if request.method=="POST":
        template_name =request.POST.get('template_name')
        field_name =request.POST.get('field_name') 
        field_type =request.POST.get('field_type')   
        isRequired =request.POST.get('isRequired') 
        data={'template_name':template_name, 'field_name':field_name, 'field_type':field_type, 'isRequired':isRequired,}
        headers={'Content-Type': 'application/json'}
        read= requests.post('http://127.0.0.1:8000/Document_details/CreateDD',json=data,headers=headers)
        
        return render(request,'insertdd.html',{"bindingid":results})
    else:
        return render(request,'insertdd.html',{"bindingid":results}) 

#pdf
def venue_pdf(request):

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",14)

    doc =Document_details.objects.all()
    lines = []

    for venue in doc:
        lines.append(str(venue.id))
        lines.append(str(venue.templateid))
        lines.append(venue.field_name)
        lines.append(venue.field_type)
        lines.append(str(venue.isRequired))
        lines.append("")

    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()  
    buf.seek(0)  

    return FileResponse(buf,as_attachment=True,filename='generatedpdf.pdf')



def template_page(request):
    results=Document_details.objects.all    
    return render(request,'templatepage.html',{"bindingid":results})
    
