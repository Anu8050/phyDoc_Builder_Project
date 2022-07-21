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
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from phyDoc_app.api import  Document_templatesCreateApi, Document_templatesListApi, Document_templatesDeleteApi, Document_templatesUpdateApi, Document_detailsCreateApi, Document_detailsListApi, Document_detailsUpdateApi, Document_detailsDeleteApi
# from phyDoc_app.views import IndexView

urlpatterns = [
    path('', include('phyDoc_app.urls')),
    path('admin/', admin.site.urls),
    path('apiend',views.insertTemplate),
    path('ddapiend/', views.insertDD),#id_binding
    path('venue_pdf',views.venue_pdf,name='venue_pdf'),
    path('template_page/', views.template_page),
    path('name/', views.new,name='new'),
    path('name_save/', views.name_save,name='name_save'),
    path('pdf/',views.pdf),
]


