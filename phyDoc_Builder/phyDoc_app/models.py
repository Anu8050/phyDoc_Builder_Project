from django.db import models


# Create your models here.
class Document_templates(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    Document_template_path = models.FileField(upload_to='Template/')
    
    def __str__(self):
        return str(self.id)
    
    def __str__(self):
        return str(self.name)
    
class Document_details(models.Model):
    id = models.AutoField(primary_key=True)
    template_name = models.ForeignKey(Document_templates,on_delete=models.SET_NULL,null=True)
    field_name = models.CharField(max_length=80)
    field_type = models.CharField(max_length=80)
    isRequired = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)



