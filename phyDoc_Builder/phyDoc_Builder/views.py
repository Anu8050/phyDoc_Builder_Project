from phyDoc_app.models import Document_templates
import requests
from django.shortcuts import render

def insert_Document_Template(request) -> any: 
    '''Rendering insert_Document_Template html page for Document_Template.'''
    if request.method=='POST':
        name=request.POST['name']   
        Document_template_path=request.FILES['Document_template_path']
        object=Document_templates.objects.create(name=name, Document_template_path=Document_template_path)
        object.save()  
    context=Document_templates.objects.all()
    return render(request,'insert_Document_Template.html',{'context':context})

def insert_Document_Details(request) -> any:
    '''Rendering insert_Document_Details html page for Document_Details.'''
    results=Document_templates.objects.all
    if request.method=="POST":
        template_name =request.POST.get('template_name')
        field_name =request.POST.get('field_name') 
        field_type =request.POST.get('field_type')   
        isRequired =request.POST.get('isRequired') 
        data={'template_name':template_name, 'field_name':field_name, 'field_type':field_type, 'isRequired':isRequired,}
        headers={'Content-Type': 'application/json'}
        read= requests.post('http://127.0.0.1:8000/Document_details/CreateDD',json=data,headers=headers)
        return render(request,'insert_Document_Details.html',{"bindingid":results})
    else:
        return render(request,'insertdd.html',{"bindingid":results}) 

def generate_Pdf_Template(request) -> any:   
    '''Rendering template_for_pdf html page for generate pdf.''' 
    results = Document_templates.objects.all()
    return render(request,'template_for_pdf.html',{'bindingid':results})
 
