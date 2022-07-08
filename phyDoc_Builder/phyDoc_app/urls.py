from django.urls import path
from .api import Document_templatesCreateApi
from . import views

urlpatterns = [
    path('api/create',Document_templatesCreateApi.as_view())
]