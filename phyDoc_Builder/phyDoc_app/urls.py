from django.urls import path
from .api import Document_templatesCreateApi, Document_templatesListApi, Document_templatesDeleteApi, Document_templatesUpdateApi
from . import views

urlpatterns = [
    path('',Document_templatesCreateApi.as_view()),
    path('api',Document_templatesListApi.as_view()),
    path('api/<int:pk>',Document_templatesUpdateApi.as_view()),
    path('api/<int:pk>',Document_templatesDeleteApi.as_view()),
]
