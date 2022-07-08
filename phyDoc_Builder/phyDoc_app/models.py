from django.db import models


# Create your models here.
class Document_templates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    Document_template_path = models.TextField(max_length=500)
    
    def __str__(self):
        return self.id

class Document_details(models.Model):
    id = models.IntegerField(primary_key=True)
    templateid = models.ForeignKey(Document_templates, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=80)
    field_type = models.CharField(max_length=80)
    isRequired = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    # def __str__(self):
    #     return str(self.id) if self.id else ''

