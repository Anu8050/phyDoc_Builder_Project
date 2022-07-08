from django.urls import path
from .api import Document_templatesCreateApi,Document_templatesUpdateApi
from . import views

urlpatterns = [
    path('api/create',Document_templatesCreateApi.as_view()),
     path('api/<int:pk>',Document_templatesUpdateApi.as_view()),
]