from django.shortcuts import render
from django.http import HttpResponse
from .models import Document_templates
from django.http import HttpResponseRedirect
from .serializer import Document_templatesSerializer

# from import handle_uploaded_file


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the phyDoc index.")

def myview(request):
    #get your list of cities you may also do some filtering 
    templatesid = [obj.id for obj in Document_templates.objects.all()]
    return render(request, 'cities_template.html', {'templatesid': templatesid})


# def upload(request):
#     if request.method == 'POST':
#         form = Document_templatesSerializer(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
            
#     else:
#         form = Document_templatesSerializer()
#     return render(request, 'core/inser.html', {
#         'form': form
#     })