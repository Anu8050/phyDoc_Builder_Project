from rest_framework import  serializers
from .models import Document_templates, Document_details

class Document_templatesSerializer(serializers.ModelSerializer):
    # item = serializers.RelatedField(many=True)
    class Meta:
        model = Document_templates
        fields = ('name','Document_template_path')
        
class Document_detailsSerializer(serializers.ModelSerializer):
    # item = serializers.RelatedField(source='category', read_only=True)
    class Meta:
        model = Document_details
        fields = ('id','field_name','field_type','isRequired','templateid')