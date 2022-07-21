from email.mime import application
import json
from django.http import HttpResponse
from wsgiref import headers
from phyDoc_app.models import Document_templates, Document_details
from phyDoc_app.serializer import Document_templatesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from django.shortcuts import render, redirect
from django.views import generic
import json
import pdfkit 

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


# def template_page(request):
#     # print("hi")
#     # results=Document_templates.objects.all #.filter(template_name_id=48).values()
#     # results = Document_details.objects.filter(template_name_id=48).values()
#     # print(type(results))
#     # for test in results:
#     #     print(test)
#     # return results
#     results = Document_details.objects.all()
#     # if request.method == 'GET':
#     #     issue_id = request.GET.get('id')
#     #     assigned = request.GET.get('assigned')
#     #     print(assigned)
#     # res=requests.get('http://127.0.0.1:8000/getbyid/{{<id>}}/').json()
    
#     # response = requests.get(placeholder_url + 'getbyid/' + str(id) + '/posts')
#     # user = response.json()
#     # context = {
#     #     'name': user
#     # }
#     # print(context)
#     # return render(request, 'templatepage.html', context,{"bindingid":results})
#     # time_series={
#     #     "field_name": "aaa",
#     #     "field_type": "int",
#     #     "isRequired": "true",
#     #     "template_name": 24
#     # }
#     # json_string = json.dumps(time_series)
#     # render(request, "foo.html", {'time_series_json_string': json_string})
    # return render(request,'templatepage.html',{'bindingid':results})
    
# def get_by_id(request):
#     res=requests.get('http://127.0.0.1:8000/getbyid/<id>/').json()
#     return render(request,'index.html',{'response':res})

def template_page(request):    
    results = Document_templates.objects.all()
    return render(request,'new20jul.html',{'bindingid':results})
 
def user_data(request):
    context = {
        "field_name": "aaa",
        "field_type": "int",
        "isRequired": "true",
        "template_name": 24
    }
    template_name="try.html"
    return render(request, template_name, context)

def new(request):
    return render(request,'new20jul.html')

def name_save(request):
    # path = "C:\Users\User\Desktop\PDB_drf\phyDoc_Builder_Project\phyDoc_Builder\Template\Template\18jul.html"
    return render(request,'21jul.html')

   
   
def pdf(request):
    projectUrl = request.get_host() + '/name_save/'
    pdf = pdfkit.from_url(projectUrl, False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'

    return response