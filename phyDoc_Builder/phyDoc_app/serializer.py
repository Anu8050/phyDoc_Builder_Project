from rest_framework import  serializers
from .models import Document_templates
class Document_templatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_templates
        fields = '__all__'