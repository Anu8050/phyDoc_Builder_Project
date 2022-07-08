from rest_framework import generics
from rest_framework.response import Response
from .serializer import Document_templatesSerializer
from .models import Document_templates

class Document_templatesCreateApi(generics.CreateAPIView):
    queryset = Document_templates.objects.all()
    serializer_class = Document_templatesSerializer