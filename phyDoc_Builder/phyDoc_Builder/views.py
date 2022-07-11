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

#generating a pdf file
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#pdf
def venue_pdf(request):

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",14)

    doc =Document_templates.objects.all()
    lines = []

    for venue in doc:
        lines.append(str(venue.id))
        lines.append(venue.name)
        lines.append(venue.Document_template_path)
        lines.append("")

    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()  
    buf.seek(0)  

    return FileResponse(buf,as_attachment=True,filename='venue1.pdf')



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


             


          


