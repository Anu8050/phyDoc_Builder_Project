from rest_framework import generics
from rest_framework.response import Response
from .serializer import Document_templatesSerializer, Document_detailsSerializer
from .models import Document_templates, Document_details

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

class Document_detailsUpdateApi(generics.RetrieveUpdateAPIView):
    queryset =  Document_details.objects.all()
    serializer_class =  Document_detailsSerializer

    


