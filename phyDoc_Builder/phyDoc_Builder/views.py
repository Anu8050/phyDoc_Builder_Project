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
from django.views import generic

#generating a pdf file
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.files.storage import FileSystemStorage

# def insertTemplate(request):
#     if request.method=="POST" and request.FILES['Document_template_path']: 
#         name=request.POST.get('name')   
#         Document_template_path=request.POST.FILES('Document_template_path') 
#         data={'name':name,'Document_template_path':Document_template_path}
#         Document_templates.objects.create(content=Document_template_path, uploader=request.user)
#         headers={'Content-Type': 'application/json'}
#         read= requests.post('http://127.0.0.1:8000/Document_templates/CreateDT',json=data,headers=headers)
#         return render(request,'insert.html')
#     else:
#         return render(request,'insert.html')  
       
# IMAGE_FILE_TYPES = ['png', 'jpg', 'txt']
# def insertTemplate(request):
#     form = Document_templatesSerializer()
#     if request.method == 'POST':
#         name=request.POST.get('name')
#         form = Document_templatesSerializer(request.POST, request.FILES)
#         Document_template_path=request.POST.get('Document_template_path')  
#         if form.is_valid():
#             user_pr = form.save(commit=False)
#             user_pr.display_picture = request.FILES['display_picture']
#             file_type = user_pr.Document_template_path.url.split('.')[-1]
#             file_type = file_type.lower()
#             if file_type not in IMAGE_FILE_TYPES:
#                 return render(request, 'insert.html')
#             user_pr.save()
#             # return render(request, '', {'user_pr': user_pr})
#             data={'name':name,'Document_template_path':Document_template_path}
#             headers={'Content-Type': 'application/json'}
#             read= requests.post('http://127.0.0.1:8000/Document_templates/CreateDT',json=data,headers=headers)
#             return render(request,'insert.html',{'user_pr': user_pr})
#     context = {"form": form,}
#     return render(request, 'insert.html', context)



# def postcreate(request):
#     if request.method == 'POST':
#         form=Document_templatesSerializer(request.POST or None,request.FILES or None)
#         files = request.FILES.getlist('file')
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             #add everything you want to add here
#             post.save()
#             if files:#check if user has uploaded some files
#                 for f in files:
#                     Document_templates.objects.create(post=post,file=f)
             
#             return redirect('the-name-of-the-view')
#     else:
#         form = Document_templatesSerializer()
#     return render(request,'the-template-you-want-to-rendered-',{'form':form})

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

# def id_binding(request):
#     results=Document_templates.objects.all
#     return render(request, "insertdd.html",{"bindingid":results})


   




