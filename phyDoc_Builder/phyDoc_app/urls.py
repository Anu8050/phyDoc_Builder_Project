from django.urls import path
from .api import  Document_templatesCreateApi, Document_templatesListApi, Document_templatesDeleteApi, Document_templatesUpdateApi, Document_detailsCreateApi, Document_detailsListApi, Document_detailsUpdateApi, Document_detailsDeleteApi
from . import views

urlpatterns = [
    path('Document_templates/CreateDT',Document_templatesCreateApi.as_view()),
    path('Document_templates/ListDT',Document_templatesListApi.as_view()),
    path('Document_templates/Update/<int:pk>',Document_templatesUpdateApi.as_view()),
    path('Document_templates/delete/<int:pk>',Document_templatesDeleteApi.as_view()),
    
    path('Document_details/CreateDD',Document_detailsCreateApi.as_view()),
    path('Document_details/ListDD',Document_detailsListApi.as_view()),
    path('Document_details/Update/<int:pk>',Document_detailsUpdateApi.as_view()),
    path('Document_details/Delete/<int:pk>',Document_detailsDeleteApi.as_view()),
 
]
