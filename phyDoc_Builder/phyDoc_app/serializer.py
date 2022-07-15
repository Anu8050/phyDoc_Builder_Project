from rest_framework import  serializers
from .models import Document_templates, Document_details

class Document_templatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_templates
        fields = ('name','Document_template_path')
        
        
class Document_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_details
        fields = ('field_name','field_type','isRequired','template_name')