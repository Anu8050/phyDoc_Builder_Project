"""phyDoc_Builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from pip import main
from . import views

urlpatterns = [
    path('', include('phyDoc_app.urls')),
    path('admin/', admin.site.urls),

    path('insert_Document_Template/',views.insert_Document_Template),
    path('insert_Document_Details/', views.insert_Document_Details),
    path('generate_Pdf_Template/', views.generate_Pdf_Template),
    path('document_templates',views.document_templates),
    path('document_details',views.document_details),
    path('read_text_file_from_template',views.readFileFromTemplate),


]


