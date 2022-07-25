from matplotlib.style import context
from rest_framework import generics
from rest_framework.response import Response
from .serializer import Document_templatesSerializer, Document_detailsSerializer
from .models import Document_templates, Document_details
from django.http import HttpResponse
from django.views.generic import View
from string import Template
import pdfkit

class Document_templatesCreateApi(generics.CreateAPIView):
    queryset = Document_templates.objects.all()
    serializer_class = Document_templatesSerializer

class Document_templatesListApi(generics.ListAPIView):
    queryset = Document_templates.objects.all()
    serializer_class = Document_templatesSerializer
    
class Document_templatesDeleteApi(generics.DestroyAPIView):
    queryset = Document_templates.objects.all()
    serializer_class = Document_templatesSerializer

class Document_templatesUpdateApi(generics.RetrieveUpdateAPIView):
    queryset =  Document_templates.objects.all()
    serializer_class = Document_templatesSerializer
    
class Document_detailsCreateApi(generics.CreateAPIView):
    queryset = Document_details.objects.all()
    serializer_class = Document_detailsSerializer

class Document_detailsListApi(generics.ListAPIView):
    queryset = Document_details.objects.all()
    serializer_class = Document_detailsSerializer
    
class Document_detailsUpdateApi(generics.RetrieveUpdateAPIView):
    queryset =  Document_details.objects.all()
    serializer_class = Document_detailsSerializer
    
class Document_detailsDeleteApi(generics.DestroyAPIView):
    queryset = Document_details.objects.all()
    serializer_class = Document_detailsSerializer
    
    
class Getobj_byId(generics.RetrieveAPIView):
    serializer_class = Document_detailsSerializer 
    model = Document_details

    def get_object(self, queryset=None) -> set:
        '''Get the object details by passing id'''
        return Document_details.objects.get(template_name=self.kwargs.get("id"))

class GeneratePdf(View):
    def get(self,request):
        ''' Api end point for generate pdf '''
        f = open("C:/Users/User/Desktop/PDB_drf/phyDoc_Builder_Project/phyDoc_Builder/Template/generate_pdf.html", "r")
        html_content = f.read()
        template = Template(html_content)
        final_html = template.substitute(name_placeholder='Anusha', age_placeholder=21, location_placeholder="rr nagar")
        config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        pdfkit.from_string(final_html, "D:/Testingpdf5.pdf", configuration=config)
        # return HttpResponse(pdfkit.from_string(final_html, "D:/Testingpdf3.pdf", configuration=config))
        return HttpResponse("Success")
        
        
        
    